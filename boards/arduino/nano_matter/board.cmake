# SPDX-License-Identifier: Apache-2.0

board_runner_args(openocd)
include(${ZEPHYR_BASE}/boards/common/openocd.board.cmake)

board_runner_args(jlink "--device=MGM240SD22VNA")
include(${ZEPHYR_BASE}/boards/common/jlink.board.cmake)
