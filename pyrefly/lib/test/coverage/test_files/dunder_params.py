# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# Tests for dunder methods with implicit parameter types.
# __exit__ params (exc_type, exc_val, exc_tb) are protocol-fixed → 0 slots.
# __getattribute__ param 0 (name: str) is implicit → 0 slots.
# Class-level __getattr__ and __setattr__ are excluded from the report entirely,
# also when defined as aliases, but public aliases of them are kept.
# Explicit annotations on implicit slots are still excluded.


class WithExit:
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class WithGetattr:
    def __getattr__(self, name):
        return None

    get = __getattr__


class WithGetattribute:
    def __getattribute__(self, name):
        return None


class WithSetattr:
    def __setattr__(self, name, value):
        pass


class AnnotatedExit:
    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> bool:
        return False


class WithNewRenamed:
    def __new__(_cls, x: int) -> "WithNewRenamed":
        return super().__new__(_cls)


class AliasedGetattr:
    def __getitem__(self, key: str) -> int:
        return 0

    __getattr__ = __getitem__


def __setattr__(name, value):
    pass
