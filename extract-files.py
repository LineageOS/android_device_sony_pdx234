#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_lib import (
    lib_fixup_vendorcompat,
    libs_proto_3_9_1,
    libs_clang_rt_ubsan,
    lib_fixup_remove_arch_suffix,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

from extract_utils.fixups_blob import (
    blob_fixups_user_type,
    blob_fixup,
)
from extract_utils.module import lib_fixups_user_type

blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/vendor.semc.hardware.extlight-V1-ndk_platform.so': blob_fixup().replace_needed(
        'android.hardware.light-V1-ndk_platform.so',
        'android.hardware.light-V1-ndk.so',
    ),
    'vendor/lib64/libarcsoft_hdr_adapter.so': blob_fixup()
    .add_needed(
        'liblog.so',
    )
    .add_needed(
        'libcutils.so',
    ),
}

lib_fixups: lib_fixups_user_type = {
    libs_proto_3_9_1: lib_fixup_vendorcompat,
    libs_clang_rt_ubsan: lib_fixup_remove_arch_suffix,
}

module = ExtractUtilsModule(
    'pdx234',
    'sony',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    check_elf=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8550-common', module.vendor
    )
    utils.run()