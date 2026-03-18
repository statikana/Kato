from abc import ABC
from dataclasses import dataclass

class ASTNode(ABC): ...

@dataclass
class Void(ASTNode):
    def __repr__(self) -> str:
        return "Void()"
    
@dataclass
class VarDef(ASTNode):
    name: str
    value: ASTNode
    
    def __repr__(self) -> str:
        return f"Def(name={self.name}, value={repr(self.value)})"


@dataclass
class VarGet(ASTNode):
    name: str
    
    def __repr__(self) -> str:
        return f"Get(name={self.name})"


@dataclass
class BinOp:
    lhs: ASTNode
    rhs: ASTNode


@dataclass
class OpAdd(ASTNode, BinOp):
    def __repr__(self):
        return f"Add(lhs={repr(self.lhs)}, rhs={repr(self.rhs)})"

@dataclass
class OpSub(ASTNode, BinOp):
    def __repr__(self):
        return f"Sub(lhs={repr(self.lhs)}, rhs={repr(self.rhs)})"

@dataclass
class OpMul(ASTNode, BinOp):
    def __repr__(self):
        return f"Mul(lhs={repr(self.lhs)}, rhs={repr(self.rhs)})"

@dataclass
class OpDiv(ASTNode, BinOp):
    def __repr__(self):
        return f"Div(lhs={repr(self.lhs)}, rhs={repr(self.rhs)})"


@dataclass
class Scope(ASTNode):
    body: list[ASTNode]

    def __repr__(self) -> str:
        return f"Scope({repr(self.body)})"
    
class Control: pass

@dataclass
class Return(ASTNode, Control):
    value: ASTNode

    def __repr__(self) -> str:
        return f"Return({repr(self.value)})"
    

@dataclass
class IfElse(ASTNode, Control):
    condition: ASTNode
    scope_true: Scope
    scope_false: Scope | None
    
    def __repr__(self):
        return f"IfElse(if={repr(self.condition)}, then={repr(self.scope_true)}, else={repr(self.scope_false)})"

@dataclass
class Emit(ASTNode, Control):
    value: ASTNode

    def __repr__(self):
        return f"Emit({repr(self.value)})"
    