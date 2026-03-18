from enum import Enum
from .ast import *
from.datatype.datatype import *
from dataclasses import dataclass, field
from typing import NamedTuple

class Control(Enum):
    RETURN = 0
    EMIT = 1

@dataclass
class Frame:
    locals: dict[str, ASTNode | None] = field(
        default_factory=lambda: {}
    )

type Stack = list[Frame] # this is python syntax?

class O(NamedTuple):
    out: ASTNode
    flags: list[Control] = []

def exec_tree(node: ASTNode, stack: Stack) -> O:
    print()
    print("exec", node)
    print("stack", stack)
    match node:
        # Control statements
        case IfElse():
            out = None
            if bool(exec_tree(node.condition, stack)):
                print("call")
                out = exec_tree(node.scope_true, stack)
            elif node.scope_false is not None:
                out = exec_tree(node.scope_false, stack)
            if out is not None and Control.RETURN in out.flags:
                return O(out.out, out.flags)
            return O(Void())
        
        case Return():
            return O(exec_tree(node.value, stack)[0], [Control.RETURN])
        
        case Emit():
            return O(exec_tree(node.value, stack)[0], [Control.EMIT])
            
        case VarDef(): # value: the set value
            # TODO: this
            value = exec_tree(node.value, stack)[0]
            if find_name(node.name, stack) is None:
                stack[-1].locals[node.name] = exec_tree(node.value, stack)[0]
            return O(value)
        
        case VarGet():
            value = find_name(node.name, stack)
            if value is None:
                print(stack)
                raise NameError(f"Name '{node.name}' not defined")
            return O(value)
        
        case BinOp():
            lhs = exec_tree(node.lhs, stack)[0]
            rhs = exec_tree(node.rhs, stack)[0]

            match node:
                case OpAdd(): return O(lhs + rhs)
                case OpSub(): return O(lhs - rhs)
                case OpMul(): return O(lhs * rhs)
                case OpDiv(): return O(lhs / rhs)
                case other: raise NotImplementedError(other)
            
            raise NotImplementedError
            
        case DataType():
            return O(node)

        case Scope():
            eval_stack = stack + [Frame()]
            emit_output: O | None = None
            for n in node.body:
                out = exec_tree(n, eval_stack)
                if Control.EMIT in out.flags:
                    emit_output = O(out.out, [])
                if Control.RETURN in out.flags:
                    return O(out.out, [Control.RETURN])
            if emit_output is not None:
                return emit_output
            else:
                return O(Void())
    
        case other:
            print(other)
            raise NotImplementedError
                
def find_name(name: str, stack: Stack):
    # prioritizes most recent
    for i in range(len(stack))[::-1]:
        if value := stack[i].locals.get(name):
            return value
    return None