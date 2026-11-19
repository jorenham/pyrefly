# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from typing import Any, Callable

class C:
    x: int
    y: str | None
    __getattr__: Callable[[str], Any]
