vendor = {
    0x0000: "Qualcomm     ",
    0x0001: "Foxconn/Sony ",
    0x0004: "ZTE          ",
    0x0011: "Smartisan    ",
    0x0015: "Huawei       ",
    0x0017: "Lenovo       ",
    0x0020: "Samsung      ",
    0x0029: "Asus         ",
    0x0030: "Haier        ",
    0x0031: "LG           ",
    0x0035: "Foxconn/Nokia",
    0x0042: "Alcatel      ",
    0x0045: "Nokia        ",
    0x0048: "YuLong       ",
    0x0051: "Oppo/Oneplus ",
    0x0072: "Xiaomi       ",
    0x0073: "Vivo         ",
    0x0130: "GlocalMe     ",
    0x0139: "Lyf          ",
    0x0168: "Motorola     ",
    0x01B0: "Motorola     ",
    0x0208: "Motorola     ",
    0x0228: "Motorola     ",
    0x2A96: "Micromax     ",
    0x02E8: "Lenovo       ",
    0x0328: "Motorola     ",
    0x0368: "Motorola     ",
    0x03C8: "Motorola     ",
    0x00C8: "Motorola     ",
    0x0348: "Motorola     ",
    0x1043: "Asus         ",
    0x1111: "Asus         ",
    0x143A: "Asus         ",
    0x1978: "Blackphone   ",
    0x2A70: "Oxygen       "
}

root_cert_hash = {
    "secboot_sha2_pss_subca1" : "afca69d4235117e5bfc21467068b20df85e0115d7413d5821883a6d244961581",
    "secboot_sha2_pss_subca2" : "d40eee56f3194665574109a39267724ae7944134cd53cb767e293d3c40497955bc8a4519ff992b031fadc6355015ac87",
    "old" : "cc3153a80293939b90d02d3bf8b23e0292e452fef662c74998421adad42a380f",
    "new" : "7be49b72f9e4337223ccb84d6eccca4e61ce16e3602ac2008cb18b75babe6d09",
    "mdm9x60_tel" : "36c886068d9a6634e9c55185044344e9e756dcc3b5960874942c7a1a1550dee0"
}

msmids = {
    # cc3153a80293939b90d02d3bf8b23e0292e452fef662c74998421adad42a380f pkhash/root-cert
    # 7be49b72f9e4337223ccb84d6eccca4e61ce16e3602ac2008cb18b75babe6d09 pkhash/root-cert
    0x9440E1: "QDF2432",
    0x9780E1: "IPQ4018",
    0x9790E1: "IPQ4019",
    0x0160E1: "QCA4020",
    0x9680E1: "APQ8009",
    0x7060E1: "APQ8016",
    0x8100E1: "APQ806x",
    0x9D00E1: "APQ8076",
    0x08A0E1: "APQ807x",
    0x9000E1: "APQ8084",
    0x9630E1: "APQ8092",
    0x0940E1: "MSM8905",
    0x9600E1: "MSM8909", # SnapDragon 210
    0x0510E1: "MSM8909W",
    0x7050E1: "MSM8916", # SnapDragon 410
    0x0560E1: "MSM8917",
    0x0860E1: "MSM8920",
    0x91B0E1: "MSM8929",  # SnapDragon 415
    0x04F0E1: "MSM8937",
    0x90B0E1: "MSM8939",  # SnapDragon 610
    0x90C0E1: "APQ8036",
    0x90D0E1: "APQ8039",
    0x06B0E1: "MSM8940",
    0x9720E1: "MSM8952",  # SnapDragon 652
    0x0460E1: "MSM8953",  # 8053lat
    0x0660E1: "APQ8053",
    0x9900E1: "MSM8976",  # SnapDragon 652
    0x9690E1: "MSM8992",  # SnapDragon 82x
    0x9400E1: "MSM8994",  # SnapDragon 808
    0x9470E1: "MSM8996",  # SnapDragon 820
    0x06F0E1: "MSM8996AU",
    0x05E0E1: "MSM8998_SDM835",
    0x94B0E1: "MSM9055",
    0x9730E1: "MDM9206_MDM9607tx",
    0x04A0E1: "MDM9607",
    0x8090E1: "MDM9916",
    0x80B0E1: "MDM9955",
    0x9210E1: "MDM9x35",
    0x9500E1: "MDM9x40",
    0x9540E1: "MDM9x45",
    0x03A0E1: "MDM9x50",
    0x7F50E1: "MDM9x25",
    0x0320E1: "MDM9250",  # MDM9x50
    0x0340E1: "MDM9255",  # MDM9x55
    0x0390E1: "MDM9350",  # MDM9x50
    0x03B0E1: "MDM9x55",
    0x07D0E1: "MDM9x60",  # SDX20
    0x07F0E1: "MDM9x65",
    0x1280E1: "fsm100xx",
    0x1650E1: "FSM10000",
    0x1680E1: "FSM10005",
    0x1690E1: "FSM10010",
    0x16A0E1: "FSM10051",
    0x16B0E1: "FSM10056",
    0x1530E1: "ipq5018",
    0x1610E1: "olympic_manar",
    0x1060E1: "qm215",
    0x0BE0E1: "SDM429",
    0x0BF0E1: "SDM439",
    0x09A0E1: "SDM450",
    0x0AC0E1: "SDM630",  #0x30070x00
    0x0BA0E1: "SDM632",
    0x0BB0E1: "SDA632",
    0x08C0E1: "SDM660",  # 0x30060000 soc_hw_version
    0x07B0E1: "SDX50M",  # 0x soc_hw_version,
    0x0E50E1: "SDX55:CD90-PG591", # 0x600b0100 soc_hw_version, 0x8fff7000 dbgpolicy 32Bit, 0x8FCFD000 sec.elf 64Bit
    0x0CF0E1: "SDX55M:CD90-PH809", # 0x600b0100 soc_hw_version, 0x8fff7000 dbgpolicy 32Bit, 0x8FCFD000 sec.elf 64Bit, # Netgear MR5100, sdxprairie
    0x1250E1: "SA515M",

    # afca69d4235117e5bfc21467068b20df85e0115d7413d5821883a6d244961581
    0x0AB0E1: "QCA6290",  # 0x40040100 soc_hw_version
    0x0D90E1: "QCA6390",  # 0x400A0000 soc_hw_version
    0x1310E1: "QCA6480",
    0x12E0E1: "QCA6481",
    0x12D0E1: "QCA6491",
    0x0D70E1: "QCA6595",  # 0x400B0000 soc_hw_version
    0x0D30E1: "QCN7605",  # 0x400B0000 soc_hw_version
    0x0D50E1: "QCN7606",  # 0x400B0000 soc_hw_version
    0x0910E1: "SDM670",  # 0x60040100 soc_hw_version
    0x0DB0E1: "SDM710",
    0x0AA0E1: "QCS605",
    0x0ED0E1: "SXR1120",
    0x0EA0E1: "SXR1130",
    0x08E0E1: "SDA845",

    # d40eee56f3194665574109a39267724ae7944134cd53cb767e293d3c40497955
    # d40eee56f3194665574109a39267724ae7944134cd53cb767e293d3c40497955bc8a4519ff992b031fadc6355015ac87 pk-hash/root-cert
    0x1260E1: "IPQ6018",
    0x1070E1: "MDM9205", # 0x20130100
    0x1450E1: "agatti", # soc_vers 0x9003
    0x13F0E1: "bitra_SDM", # soc_vers 0x6012 SDM690
    0x1410E1: "bitra_SDA",
    0x1590E1: "cedros", # soc_vers 0x6017
    0x1360E1: "kamorta", # soc_vers 0x9002 SnapDragon 662/460 SM4250/SM4350, bengal
    0x1350E1: "lahaina", # soc_vers 0x600F sm8350, SDM875
    0x1420E1: "lahaina_premier",
    0x14A0E1: "makena", # soc_vers 0x6014
    0x14B0E1: "SA8295P",
    0x14C0E1: "SA8540P",
    #0x1610E1: "mannar", # soc_vers 0x9004
    0x1470E1: "moselle", # soc_vers 0x4014
    0x10A0E1: "nicobar",  # 0x90010100 soc_hw_version, 0x45FFF000 sec.elf 64Bit, 0x101FF000 dbgpolicy, 64Bit
    0x10B0E1: "qcn90xx", # soc_vers 0x400D
    0x10C0E1: "QCN9001",
    0x1150E1: "QCN9002",
    0x10D0E1: "QCN9003",
    0x10E0E1: "QCN9010",
    0x10F0E1: "QCN9011",
    0x1110E1: "QCN9012",
    0x1140E1: "QCN9013",
    0x0AF0E1: "qcs405",  # 0x20140000 soc_hw_version, 0x863DB000 sec.elf 64Bit, 0x863DE000 dbgpolicy, 64Bit
    0x0400E1: "rennell", # soc_vers 0x600E7T A11 CB
    0x12A0E1: "rennell",
    0x12B0E1: "rennell_premier",
    0x1490E1: "rennell_v1.1",
    0x1630E1: "sd7250",
    0x11E0E1: "saipan", # 0x600D0100 soc_hw_version, 0x808FF000 sec.elf 64Bit, 0x1C000000 dbgpolicy, 64Bit, SM7250 Snapdragon 765G
    0x0950E1: "SM6150",  # 0x60070100 soc_hw_version, 0x85FFF000 sec.elf 64Bit, 0x1C1FF000 dbgpolicy, 64Bit
    0x0EC0E1: "SM6150p",  # 0x60070100 soc_hw_version, 0x85FFF000 sec.elf 64Bit, 0x1C1FF000 dbgpolicy, 64Bit
    0x0E60E1: "SM7150",  # 0x600C0100 soc_hw_version, 0x85FFF000 sec.elf 64Bit, 0x1C1FF000 dbgpolicy, 64Bit
    0x0A50E1: "SDM855_SM8150", # Hana 0x60030100 soc_hw_version, 0x85FFF000 sec.elf 64Bit, 0x1C1FF000 dbgpolicy, 64Bit
    0x0A60E1: "SDM855p_SM8150p", # Hana 0x60030100 soc_hw_version, 0x85FFF000 sec.elf 64Bit, 0x1C1FF000 dbgpolicy, 64Bit
    0x0C30E1: "SM8250:CD90-PH805-1A", # Kona, 0x60080100 soc_hw_version, 0x808FF000 sec.elf 64Bit, 0x1C000000 dbgpolicy, 64Bit
    0x0CE0E1: "SM8250:CD90-PH806-1A", # Kona 0x60080100 soc_hw_version, 0x808FF000 sec.elf 64Bit, 0x1C000000 dbgpolicy, 64Bit
    0x0B80E1: "sc8180x", # Snapdragon 8CX
    0x1560E1: "SM8250", # HDK 8250
    0x1510e1: "SA2150p",

    # Unknown root hash
    0x0B70E1: "SDM850",
    0x0960E1: "SDX24",  # 0x60020100 soc_hw_version, 0x8fff7000 dbgpolicy 32Bit, 0x8FCFD000 sec.elf 64Bit
    0x0970E1: "SDX24M", # 0x60020100 soc_hw_version, 0x8fff7000 dbgpolicy 32Bit, 0x8FCFD000 sec.elf 64Bit
    0x0E70E1: "SM7150p", # 0x600C0100 soc_hw_version, 0x85FFF000 sec.elf 64Bit, 0x1C1FF000 dbgpolicy, 64Bit
    0x0E80E1: "SA8155", # 0x60030100 soc_hw_version, 0x85FFF000 sec.elf 64Bit, 0x1C1FF000 dbgpolicy, 64Bit
    0x0E90E1: "SA8155p", # 0x60030100 soc_hw_version, 0x85FFF000 sec.elf 64Bit, 0x1C1FF000 dbgpolicy, 64Bit
    0x0E40E1: "qcs403", # 0x20140000 soc_hw_version, 0x863DB000 sec.elf 64Bit, 0x863DE000 dbgpolicy, 64Bit
    0x1440E1: "chitwan", # soc_vers 0x6013
    0x1370E1: "kamortap",
    0x6220E1: "MSM7227A",
    0x8040E1: "APQ8026",
    0x0550E1: "APQ8017",
    0x90F0E1: "APQ8037",
    0x9770E1: "APQ8052",
    0x9F00E1: "APQ8056",
    0x7190E1: "APQ8064",
    0x9300E1: "APQ8092",
    0x0620E1: "APQ8098",
    0x8110E1: "MSM8210",
    0x8140E1: "MSM8212",
    0x8120E1: "MSM8610",
    0x8150E1: "MSM8612",
    0x8010E1: "MSM8626",
    0x8050E1: "MSM8926", # SnapDragon 400
    0x9180E1: "MSM8928", # SnapDragon 400
    0x7210E1: "MSM8930",
    0x72C0E1: "MSM8960",
    0x9B00E1: "MSM8956", # SnapDragon 652
    0x9100E1: "MSM8962",
    0x7B00E1: "MSM8974", # Snapdragon 800
    0x7B30E1: "MSM8974A",
    0x7B40E1: "MSM8974AB",
    0x7B80E1: "MSM8974Pro",
    0x7BC0E1: "MSM8974ABv3",
    0x6B10E1: "MSM8974AC",
    0x05F0E1: "MSM8996Pro", # SnapDragon 821
    0x0480E1: "MDM9207",
    0x0CC0E1: "SDM636",
    0x0930E1: "SDA670",  # 0x60040100 soc_hw_version
    #0x0930E1: "SDA835", # 0x30020000 => HW_ID1 3002000000290022
    0x08B0E1: "SDM845",  # Napali 0x60000100 => HW_ID1 6000000000010000
    #SDM840 NapaliQ ?
    #SDM640 Talos ?
}

sochw = {
    0x2013: "MDM9205",
    0x2014: "qcs405",
    0x2017: "IPQ6018",
    0x3002: "MSM8998_SDM835,SDA835",
    0x3006: "SDM660",
    0x3007: "SDM630",
    0x4003: "QCA4020",
    0x4004: "IPQ8074,QCA6290",
    0x400A: "QCA6390",
    0x400B: "QCN7605,QCA6595,QCN7606",
    0x400D: "qcn90xx",
    0x4014: "moselle",

    #: "SDM632",
    #: "SDA632",
    #: "SDM636",
    0x6000: "SDM845",
    0x6001: "SDA845",
    0x6002: "SDX24,SDX24M",
    0x6003: "SDM855_SM8150,SDM855p_SM8150p",
    0x6004: "SDA670,SDM670,SDM710",
    0x6005: "SDM670",
    #: "SDX50M",
    0x6006: "sc8180x",
    0x6007: "SM6150,SM6150p",
    0x6008: "SM8250:CD90-PH805-1A,SM8250:CD90-PH806-1A,SM8250",
    0x6009: "SDM670",
    0x600B: "SDX55:CD90-PG591,SDX55:CD90-PH809",
    0x600C: "SM7150,SM7150p",
    0x600D: "saipan",
    0x600E: "rennell",
    0x600F: "lahaina",
    0x6012: "bitra_SDM",
    0x6013: "chitwan",
    0x6014: "makena",
    0x6016: "olympic",
    0x6017: "cedros",
    0x9001: "nicobar",
    0x9002: "kamorta",
    0x9003: "agatti",
    0x9004: "mannar"
}

secgen=[
    # BOOT_ROM_BASE_PHYS, SECURITY_CONTROL_BASE_PHYS, MEMORY_MAP
    [[], [0x01900000, 0x100000], []],
    [[],[0x01e20000,0x1000],[]],
    [[0xFC010000, 0x18000], [0xFC4B8000, 0x60F0], [0x200000, 0x24000]],
    [[0x100000, 0x1ffb0], [0x70000, 0x6158], [0x200000, 0x24000]],
    [[0x100000, 0x1ffb0], [0x00058000, 0x1000], [0x200000, 0x24000]],
    [[0x100000, 0x1ffb0], [0x000A0000, 0x6FFF], [0x200000, 0x24000]],
    [[0x100000, 0x1ffb0], [0x00700000, 0x6158], [0x200000, 0x24000]],
    [[0x300000, 0x3c000], [0x00780000, 0x10000], [0x14009003, 0x24000]],
    [[0x300000, 0x3c000], [0x01B40000, 0x10000], []],
]

infotbl = {
    "QDF2432": secgen[0],
    "QCA6290": secgen[1],
    "QCA6390": secgen[1],
    "QCA6480": secgen[1],
    "QCA6481": secgen[1],
    "QCA6490": secgen[1],
    "QCA6491": secgen[1],

    "APQ8084": secgen[2],
    "APQ8092": secgen[2],
    "MSM8962": secgen[2],
    "MSM8974": secgen[2],
    "MSM8974Pro": secgen[2],
    "MSM8974AB": secgen[2],
    "MSM8974ABv3": secgen[2],
    "MSM8974AC": secgen[2],
    "MSM8992": secgen[2],
    "MSM8994": secgen[2],
    "MDM9x25": secgen[2],
    "MDM9x35": secgen[2],

    "MSM8996": secgen[3],
    "MSM8996AU": secgen[3],
    "MSM8996Pro": secgen[3],

    "IPQ4018": secgen[4],
    "IPQ4019": secgen[4],
    "APQ8009": secgen[4],
    "APQ8016": secgen[4],
    "APQ8036": secgen[4],
    "APQ8039": secgen[4],
    "MSM8905": secgen[4],
    "MSM8909": secgen[4],
    "MSM8909W": secgen[4],
    "MSM8916": secgen[4],
    "MSM8929": secgen[4],
    "MSM8939": secgen[4],
    "MSM8952": secgen[4],
    "MDM9x40": secgen[4],
    "MDM9x45": secgen[4],

    "APQ8017": secgen[5],
    "APQ8037": secgen[5],
    "APQ8053": secgen[5],
    "APQ8056": secgen[5],
    "APQ8076": secgen[5],
    "MSM8917": secgen[5],
    "MSM8920": secgen[5],
    "MSM8937": secgen[5],
    "MSM8940": secgen[5],
    "MSM8953": secgen[5],
    "MSM8956": secgen[5],
    "MSM8976": secgen[5],
    "MSM9206": secgen[5],
    "MDM9207": secgen[5],
    "MDM9607": secgen[5],
    "MDM9x50": secgen[5],
    "MDM9x55": secgen[5],
    "MDM9x60": secgen[5],
    "MDM9x65": secgen[5],
    "MDM9250": secgen[5],
    "MDM9350": secgen[5],
    "MDM9650": secgen[5],
    "SDM429": secgen[5],
    "SDM439": secgen[5],
    "SDM450": secgen[5],
    "SDM632": secgen[5],
    "SDA632": secgen[5],
    "SDX50M": secgen[5],
    "qcs403": secgen[5],
    "qcs405": secgen[5],
    "ipq5018": secgen[5],
    "ipq6018": secgen[5],
    "qm215": secgen[5],

    "APQ806x": secgen[6],
    "MSM8930": secgen[6],
    "MSM8936": secgen[6],

    "APQ8098": secgen[7],
    "MSM8998": secgen[7],
    "SDM630": secgen[7],
    "SDM636": secgen[7],
    "SDM660": secgen[7],
    "SDM670": secgen[7],
    "SDA670": secgen[7],
    "SDM710": secgen[7],
    "QCS605": secgen[7],
    "SXR1120": secgen[7],
    "SXR1130": secgen[7],
    "SDM845": secgen[7],
    "SDA845": secgen[7],
    "SDM850": secgen[7],
    "SDX24": secgen[7],
    "SDX24M": secgen[7],
    "SDX55M": secgen[7],
    "SDX55:CD90-PG591": secgen[7],
    "SDX55:CD90-PH809": secgen[7],
    "SA515M": secgen[7],
    "SM6150": secgen[7],
    "SM6150p": secgen[7],
    "SM7150": secgen[7],
    "SM7150p": secgen[7],
    "SDM855_SM8150": secgen[7],
    "SDM855p_SM8150p": secgen[7],
    "SA2150p": secgen[7],
    "SM8250": secgen[7],
    "SM8250p": secgen[7],
    "SM8250:CD90-PH805-1A": secgen[7],
    "SM8250:CD90-PH806-1A": secgen[7],
    "saipan": secgen[7],
    "sc8180x": secgen[7],
    "bitra": secgen[7],
    "cedros": secgen[7],
    "chitwan": secgen[7],
    "lahaina": secgen[7],
    "lahaina_premier": secgen[7],
    "mannar": secgen[7],
    "rennell": secgen[7],
    "sd7250": secgen[7],

    "nicobar": secgen[8],
    "agatti": secgen[8],
    "kamorta": secgen[8],
    "kamortap": secgen[8],


    # "MSM7227A": [[], [], []],
    # "MSM8210": [[], [0xFC4B8000,0x6FFF], []],
    # "MSM8212": [[], [], []],
    # "MSM8610": [[], [0xFC4B8000,0x6FFF], []],
    # "MSM8226": [[], [0xFC4B8000,0x6FFF], []],
    # "MSM8926": [[], [0xFC4B8000,0x6FFF], []],
    # "MSM8928": [[], [], []],
}

class memory_type:
    nand = 0
    emmc = 1
    ufs = 2
    spinor = 3

    preferred_memory = {
        "QDF2432": emmc,
        "QCA6290": emmc,
        "QCA6390": emmc,
        "QCA6480": emmc,
        "QCA6481": emmc,
        "QCA6490": emmc,
        "QCA6491": emmc,

        "APQ8084": emmc,
        "APQ8092": emmc,
        "MSM8962": emmc,
        "MSM8974": emmc,
        "MSM8974Pro": emmc,
        "MSM8974AB": emmc,
        "MSM8974ABv3": emmc,
        "MSM8974AC": emmc,
        "MSM8992": emmc,
        "MSM8994": emmc,
        "MDM9x25": emmc,
        "MDM9x35": emmc,

        "MSM8996": ufs,
        "MSM8996AU": ufs,
        "MSM8996Pro": ufs,

        "IPQ4018": emmc,
        "IPQ4019": emmc,
        "APQ8009": emmc,
        "APQ8016": emmc,
        "APQ8036": emmc,
        "APQ8039": emmc,
        "MSM8905": emmc,
        "MSM8909": emmc,
        "MSM8909W": emmc,
        "MSM8916": emmc,
        "MSM8929": emmc,
        "MSM8939": emmc,
        "MSM8952": emmc,
        "MDM9x40": emmc,
        "MDM9x45": emmc,

        "APQ8017": emmc,
        "APQ8037": emmc,
        "APQ8053": emmc,
        "APQ8056": emmc,
        "APQ8076": emmc,
        "MSM8917": emmc,
        "MSM8920": emmc,
        "MSM8937": emmc,
        "MSM8940": emmc,
        "MSM8953": emmc,
        "MSM8956": emmc,
        "MSM8976": emmc,
        "MSM9206": emmc,
        "MDM9207": nand,
        "MDM9607": nand,
        "MDM9x50": emmc,
        "MDM9x55": emmc,
        "MDM9x60": emmc,
        "MDM9x65": emmc,
        "MDM9250": emmc,
        "MDM9350": emmc,
        "MDM9650": emmc,
        "SDM429": emmc,
        "SDM439": emmc,
        "SDM450": emmc,
        "SDM632": emmc,
        "SDA632": emmc,
        "SDX50M": emmc,
        "qcs403": emmc,
        "qcs405": emmc,
        "ipq5018": emmc,
        "ipq6018": emmc,
        "qm215": emmc,

        "APQ806x": emmc,
        "MSM8930": emmc,
        "MSM8936": emmc,

        "APQ8098": emmc,
        "MSM8998": ufs,
        "SDM630": emmc,
        "SDM636": emmc,
        "SDM660": emmc,
        "SDM670": emmc,
        "SDA670": emmc,
        "SDM710": emmc,
        "QCS605": emmc,
        "SXR1120": emmc,
        "SXR1130": emmc,
        "SDM845": ufs,
        "SDA845": ufs,
        "SDM850": ufs,
        "SDX24": emmc,
        "SDX24M": emmc,
        "SDX55M": ufs,
        "SDX55:CD90-PG591": ufs,
        "SDX55:CD90-PH809": ufs,
        "SA515M": emmc,
        "SM6150": emmc,
        "SM6150p": emmc,
        "SM7150": emmc,
        "SM7150p": emmc,
        "SDM855_SM8150": ufs,
        "SDM855p_SM8150p": ufs,
        "SM8250": ufs,
        "SM8250p": ufs,
        "SM8250:CD90-PH805-1A": ufs,
        "SM8250:CD90-PH806-1A": ufs,
        "saipan": ufs,
        "sc8180x": ufs,
        "bitra": ufs,
        "cedros": ufs,
        "chitwan": ufs,
        "lahaina": ufs,
        "lahaina_premier": ufs,
        "mannar": ufs,
        "rennell": ufs,
        "sd7250": ufs,
        "SA2150p": emmc,

        "nicobar": ufs,
        "agatti": ufs,
        "kamorta": ufs,
        "kamortap": ufs,

        # "MSM7227A": [[], [], []],
        # "MSM8210": [[], [0xFC4B8000,0x6FFF], []],
        # "MSM8212": [[], [], []],
        # "MSM8610": [[], [0xFC4B8000,0x6FFF], []],
        # "MSM8226": [[], [0xFC4B8000,0x6FFF], []],
        # "MSM8926": [[], [0xFC4B8000,0x6FFF], []],
        # "MSM8928": [[], [], []],
    }


secureboottbl = {
    "QDF2432": 0x019018c8,
    "QCA6290": 0x01e20030,
    "QCA6390": 0x01e20010,
    "IPQ4018": 0x00058098,
    "IPQ4019": 0x00058098,
    "APQ8009": 0x00058098,
    "APQ8016": 0x00058098,
    "APQ8036": 0x00058098,
    "APQ8039": 0x00058098,
    "APQ8037": 0x000a01d0,
    "APQ8053": 0x000a01d0,
    "APQ8052": 0x00058098,
    "APQ8056": 0x000a01d0,
    "APQ8076": 0x000a01d0,
    "APQ8084": 0xFC4B83F8,
    "APQ8092": 0xFC4B83F8,
    "APQ8098": 0x00780350,
    "MSM8226": 0xFC4B83E8,
    "MSM8610": 0xFC4B83E8,
    "MSM8905": 0x00058098,
    "MSM8909": 0x00058098,
    "MSM8909W": 0x00058098,
    "MSM8916": 0x00058098,
    "MSM8917": 0x000A01D0,
    "MSM8920": 0x000A01D0,
    "MSM8929": 0x00058098,
    "MSM8930": 0x700310,
    "MSM8936": 0x700310,
    "MSM8937": 0x000A01D0,
    "MSM8939": 0x00058098,
    "MSM8940": 0x000A01D0,
    "MSM8952": 0x00058098,
    "MSM8953": 0x000a01d0,
    "MSM8956": 0x000a01d0,
    "MSM8974": 0xFC4B83F8,
    "MSM8974AB": 0xFC4B83F8,
    "MSM8974ABv3": 0xFC4B83F8,
    "MSM8974AC": 0xFC4B83F8,
    "MSM8976": 0x000a01d0,
    "MSM8992": 0xFC4B83F8,
    "MSM8994": 0xFC4B83F8,
    "MSM8996": 0x00070378,
    "MSM8996AU": 0x00070378,
    "MSM8996Pro": 0x00070378,
    "MSM8998_SDM835": 0x00780350,
    "MDM9205": 0x000a0320,
    "MDM9206_MDM9207tx": 0x000a01d0,
    "MDM9250": 0x000a01d0,
    "MDM9350": 0x000a01d0,
    "MDM9207": 0x000a01d0,
    "MDM9607": 0x000a01d0,
    "MDM9x25": 0xFC4B6028,
    "MDM9x30": 0xFC4B6028,
    "MDM9x35": 0xFC4B6028,
    "MDM9x40": 0x00058098,
    "MDM9x45": 0x00058098,
    "MDM9650": 0x000a01d0,
    "MDM9x50": 0x000a01d0,
    "MDM9x55": 0x000a01d0,
    "MDM9x60": 0x000a01d0,
    "MDM9x65": 0x000a01d0,
    "SDM429": 0x000a01d0,
    "SDM439": 0x000a01d0,
    "SDM450": 0x000a01d0,
    "SDM630": 0x00780350,
    "SDM632": 0x000a01d0,
    "SDA632": 0x000a01d0,
    "SDM636": 0x00780350,
    "SDM660": 0x00780350,
    "SDM670": 0x00780350, # Warlock
    "SDA670": 0x00780350,
    "SDM710": 0x00780350,
    "QCS605": 0x00780350,
    "SXR1120": 0x00780350,
    "SXR1130": 0x00780350,
    "SDM845": 0x00780350,
    "SDA845": 0x00780350,
    "SDX24" : 0x00780390,
    "SDX24M": 0x00780390,
    "SDX50M": 0x000a01e0,
    "SDX55:CD90-PG591":  0x007805E8,
    "SDX55:CD90-PH809":  0x007805E8,
    "SDX55M" : 0x007804D0,
    "SA515M" : 0x007804D0,
    "SM6150": 0x00780360,
    "SM6150p": 0x00780360,
    "SM7150": 0x00780460,
    "SM7150p": 0x00780460,
    "SDM855_SM8150": 0x007804D0,
    "SDM855p_SM8150p": 0x007804D0,
    "SA2150p": 0x7804D0,
    "SM8250:CD90-PH805-1A": 0x007805E8,
    "SM8250:CD90-PH806-1A": 0x007805E8,
    "agatti": 0x01B40458,
    "bitra": 0x007804D8,
    "bitra_SDM": 0x007804D8,
    "bitra_SDA": 0x007804D8,
    "cedros": 0x00780728,
    "chitwan": 0x00780668,
    "ipq5018": 0x000A01D0,
    "ipq6018": 0x000A01D0,
    "saipan": 0x007805E8,
    "sd7250": 0x007805E8,
    "sc8180x": 0x007805E8,
    "qcs403": 0x000a0310,
    "qcs405": 0x000a0310,
    "nicobar": 0x01B40458,
    "kamorta": 0x01B40458,
    "kamorta_p": 0x01B40458,
    "lahaina": 0x780668,
    "lahaina_premier": 0x780668,
    "mannar": 0x01B40458,
    "qm215": 0x000a01d0,
    "rennell":0x000780498
    # "MSM7227A":[[], [], []],
    # "MSM8210": [[], [], []],
    # "MSM8212":
    # "MSM8926": [[], [], []],
    # "MSM8928": [[], [], []],
}
