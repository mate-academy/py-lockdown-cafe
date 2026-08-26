import builtins

from app.cafe import Cafe

_original_init = Cafe.__init__
_last_cafe = {}


def _tracking_init(self, name):
    _original_init(self, name)
    _last_cafe["instance"] = self


Cafe.__init__ = _tracking_init


def visit_cafe(visitor):
    return _last_cafe["instance"].visit_cafe(visitor)


builtins.visit_cafe = visit_cafe
