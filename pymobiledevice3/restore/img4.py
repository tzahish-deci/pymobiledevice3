def img4_get_component_tag(compname):
    component_tags = {
        'ACIBT': b'acib',
        'ACIBTLPEM': b'lpbt',
        'ACIWIFI': b'aciw',
        'Alamo': b'almo',
        'ANE': b'anef',
        'ANS': b'ansf',
        'AOP': b'aopf',
        'Ap,AudioAccessibilityBootChime': b'auac',
        'Ap,AudioBootChime': b'aubt',
        'Ap,AudioPowerAttachChime': b'aupr',
        'Ap,CIO': b'ciof',
        'Ap,HapticAssets': b'hpas',
        'Ap,LocalBoot': b'lobo',
        'Ap,LocalPolicy': b'lpol',
        'Ap,NextStageIM4MHash': b'nsih',
        'Ap,RecoveryOSPolicyNonceHash': b'ronh',
        'Ap,RestoreCIO': b'rcio',
        'Ap,RestoreTMU': b'rtmu',
        'Ap,Scorpius': b'scpf',
        'Ap,TMU': b'tmuf',
        'Ap,VolumeUUID': b'vuid',
        'AppleLogo': b'logo',
        'AudioCodecFirmware': b'acfw',
        'AVE': b'avef',
        'BatteryCharging': b'glyC',
        'BatteryCharging0': b'chg0',
        'BatteryCharging1': b'chg1',
        'BatteryFull': b'batF',
        'BatteryLow0': b'bat0',
        'BatteryLow1': b'bat1',
        'BatteryPlugin': b'glyP',
        'CFELoader': b'cfel',
        'Dali': b'dali',
        'DCP': b'dcpf',
        'DeviceTree': b'dtre',
        'Diags': b'diag',
        'EngineeringTrustCache': b'dtrs',
        'ExtDCP': b'edcp',
        'ftap': b'ftap',
        'ftsp': b'ftsp',
        'GFX': b'gfxf',
        'Hamm': b'hamf',
        'Homer': b'homr',
        'iBEC': b'ibec',
        'iBoot': b'ibot',
        'iBootData': b'ibdt',
        'iBootTest': b'itst',
        'iBSS': b'ibss',
        'InputDevice': b'ipdf',
        'ISP': b'ispf',
        'KernelCache': b'krnl',
        'LeapHaptics': b'lphp',
        'Liquid': b'liqd',
        'LLB': b'illb',
        'LoadableTrustCache': b'ltrs',
        'LowPowerWallet0': b'lpw0',
        'LowPowerWallet1': b'lpw1',
        'LowPowerWallet2': b'lpw2',
        'MacEFI': b'mefi',
        'Multitouch': b'mtfw',
        'NeedService': b'nsrv',
        'OS': b'OS\0\0',
        'OSRamdisk': b'osrd',
        'PersonalizedDMG': b'pdmg',
        'PEHammer': b'hmmr',
        'PERTOS': b'pert',
        'PHLEET': b'phlt',
        'PMP': b'pmpf',
        'RBM': b'rmbt',
        'Rap,SoftwareBinaryDsp1': b'sbd1',
        'Rap,RTKitOS': b'rkos',
        'Rap,RestoreRTKitOS': b'rrko',
        'RecoveryMode': b'recm',
        'RestoreANS': b'rans',
        'RestoreDCP': b'rdcp',
        'RestoreDeviceTree': b'rdtr',
        'RestoreExtDCP': b'recp',
        'RestoreKernelCache': b'rkrn',
        'RestoreLogo': b'rlgo',
        'RestoreRamDisk': b'rdsk',
        'RestoreSEP': b'rsep',
        'RestoreTrustCache': b'rtsc',
        'rfta': b'rfta',
        'rfts': b'rfts',
        'RTP': b'rtpf',
        'SCE': b'scef',
        'SCE1Firmware': b'sc1f',
        'SEP': b'sepi',
        'SIO': b'siof',
        'StaticTrustCache': b'trst',
        'SystemLocker': b'lckr',
        'WCHFirmwareUpdater': b'wchf',
    }

    return component_tags.get(compname)