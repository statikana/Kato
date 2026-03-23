from enum import Enum
from .ast import *
from .datatype.datatype import *
from dataclasses import dataclass, field
from typing import NamedTuple

class Flag(Enum):
    RETURN = 0
    EMIT = 1

@dataclass
class Frame:
    locals: dict[str, DataType] = field(
        default_factory=lambda: {}
    )

@dataclass
class Closure(DataType):  # hmm...
    name: str
    stack: Stack
    scope: Scope
    args: list[str]

type Stack = list[Frame] # this is python syntax?

@dataclass
class Out:
    value: ASTNode
    flags: list[Flag] = field(default_factory=lambda: [])


def exec_tree(node: ASTNode, stack: Stack) -> Out:
    print("exec", node)
    match node:
        # Control statements
        case IfElse():
            out = None
            if bool(exec_tree(node.condition, stack)):
                out = exec_tree(node.scope_true, stack)
            elif node.scope_false is not None:
                out = exec_tree(node.scope_false, stack)
            if out is not None and Flag.RETURN in out.flags:
                return Out(out.value, out.flags)
            return Out(Void())
        
        case Return():
            return Out(exec_tree(node.value, stack).value, [Flag.RETURN])
        
        case Emit():
            return Out(exec_tree(node.value, stack).value, [Flag.EMIT])
            
        case VarDef():
            value = exec_tree(node.value, stack).value
            define(node.name, value, stack)
            return Out(value)
        
        case VarGet():
            value = find_name(node.name, stack)
            if value is None:
                raise NameError(f"Name '{node.name}' not defined")
            return Out(value)
        
        case BinOpNode():
            lhs = exec_tree(node.lhs, stack).value
            rhs = exec_tree(node.rhs, stack).value

            match node:
                case OpAdd(): return Out(lhs + rhs)
                case OpSub(): return Out(lhs - rhs)
                case OpMul(): return Out(lhs * rhs)
                case OpDiv(): return Out(lhs / rhs)
                case other: raise NotImplementedError(other)
            
            raise NotImplementedError
            
        case DataType():
            return Out(node)

        case Scope():
            eval_stack = stack + [Frame()]
            emit_output: Out | None = None
            for n in node.body:
                out = exec_tree(n, eval_stack)
                if Flag.EMIT in out.flags:
                    emit_output = Out(out.value, [])
                if Flag.RETURN in out.flags:
                    return Out(out.value, [Flag.RETURN])
            if emit_output is not None:
                return emit_output
            else:
                return Out(Void())
        
        case FunctionDef():
            closure = Closure(
                name=node.name,
                stack=stack.copy(),
                scope=node.scope,
                args=node.args
            )
            define(node.name, closure, stack)

            return Out(closure)

        case Call():
            called = exec_tree(node.value, stack).value
            if not isinstance(called, Closure):
                raise ValueError(f"{called} is not a function")
            
            func_stack = called.stack + [Frame()]
            if len(called.args) != len(node.args):
                raise ValueError(f"Arg mismatch: '{called.name}' takes {len(called.args)} arguments, {len(node.args)} provided")
            for name, value in zip(called.args, node.args):
                define(name, value, func_stack)
            output = exec_tree(called.scope, func_stack)
            # we don't propagate any Flag.RETURN signals here
            return Out(output.value, flags=[]) 
        
        case other:
            raise NotImplementedError
                
def find_name(name: str, stack: Stack) -> DataType | None:
    # prioritizes most recent
    for i in range(len(stack))[::-1]:
        if (value := stack[i].locals.get(name)) is not None:
            return value
    return None

def define(name: str, value: DataType, stack: Stack) -> None:
    for i in range(len(stack))[::-1]:
        if name in stack[i].locals.keys():
            stack[i].locals[name] = value
            return
    stack[-1].locals[name] = value