import binascii
import struct


def parseData(data):
    v = int(data[0])
    if v >= 0x40 and v < 0x80 or v >= 0xc0:
        return 0x40 - parseData2(data)
    else:
        return parseData2(data)

def parseData2(data):
    nBytes = 0
    while int(data[nBytes]) >= 0x80:
        nBytes += 1

    nBytes += 1

    if nBytes == 1:
        return int(data[0])
    elif nBytes == 2:
        return (int(data[1]) * 0x40 + int(data[0])) - 0x80
    elif nBytes == 3:
        return (int(data[2]) * 0x80 + int(data[1]) - 0x80) * 0x40 + int(data[0]) - 0x80
    elif nBytes == 4:
        return ((int(data[3]) * 0x80 + int(data[2]) - 0x80) * 0x80 + int(data[1] - 0x80)) * 0x40 + int(data[0]) - 0x80
    elif nBytes == 5:
        return (((int(data[4]) * 0x80 + int(data[3]) - 0x80) * 0x80 + int(data[2]) - 0x80) * 0x80 + int(data[1]) - 0x80)* 0x40 + int(data[0]) - 0x80
    elif nBytes == 6:
        return ((((int(data[5]) * 0x80 + int(data[4]) -0x80) * 0x80 +  int(data[3]) - 0x80) * 0x80 + int(data[2]) - 0x80) * 0x80 + int(data[1]) - 0x80) * 0x40 + int(data[0]) - 0x80
    else:
        assert False


data = binascii.unhexlify(b'1801ff695d03b0c101000a5400a82c4750c90549ff695e03000028000088db46c03caa48ff695f03281e1e5e0020644640963148ff6960034a1e1e0000f0874640335448ff696103541e1e000050114600dae247ff6962034a0000000040034500eacc46ff6963030054005400a0f04580b7bb47ff6964030a4a0a4a0020cb4580649e47ff69650300000a0000808945005e5647ff696603000000000070784640a04148ff696703544a00720000164500bae846ff6968035e0a0a000040034500accb46ff6969031e00005e00100b468066d847ff696a030a14140000100b4600b9d847ff696b030a0a0a00002000468023c847ff696c031e14140000c0c14580c69747ff696d030a00004a0020e4458011b347ff696e034a0000720058984680bc6e48ff696f030a0a1e4a00f0204600dffc47ff6970034a141e0000704646c0011c48ff6971034a4a0a4a0010564600332848ff69720300001400005011460046e447ff69730300141e0000c00f460012e247ff6974030a4a0a4a0048a346207b8048ff697503000a0a000060ea458053b847ff697603004a004a007014468091e947ff69770300000a000060b84500f89047ff6978034a4a004a0010244600db0048ff697903005e0a5e00e8804680124a48ff697a0300000a000000484500b11c47ff697b031400004a0070144680d2e847ff697c034a0a0a000000484500d61c47ff697d03004a004a0050434600271948ff697e030a0a0a540058b146e0f68a48ff697f03005400540040834500084e47ff6980030a4a004a00f05246806b2548ff69810300000a0000709446c0c06848ff698203000000000000484300c01c45ff698303000000000000000000000000ff6984030a00000000f0b94640d89148006a3b0200cc0200d60200189246c01a6348006a3c02289a019a01000000964400b86946006a3d02000a0ad00100c0414500d31747006a3e020028280000803b45003e1347006a3f0214001e000000af4400228a46006a40024a72007200106f4680b33b48006a410200001e0000088446004a4f48006a4202145400540080544500ca2647006a43020a3232000000964400f86b46006a44020a1e1e0000e02b46c0bc0748006a45020a860190010000702d4680cf0948006a4602007200720070144680bdeb47006a4702140a1e0000a02546c0ac0348006a48021400005400502a4640780748006a4902005400540058b146e0e78c48006a4a0200000a4a00d0684680f03848006a4b02004a004a00e01246002ce947006a4c02004a005400505c4640cb2e48006a4d02004a004a0000af46e0b38a48006a4e02005400540040ce46e06ba348006a4f024a5e005e00c0a845005b8547006a5002000a14000020804600264a48006a51020a0a144a00a03e46c0a51648006a5202000a0a000060864500885447006a53020a14140000c0414600951948006a54024a000a000088db462000ae48006a55024a4a004a000016450088ed46006a5602001e1e0000b01a46003af547006a57025e141e000040834500125047006a5802000a0a0000e0ab45803a8847006a590200000a0000805446c0902848006a5a0200000a0000a89346403a6a48006a5b024a0a0a0000408345000d5047006a5c02004a00540060ea4500d5b947006a5d024a00140000e0f645009cc347006a5e02001414000040e7458056b747006a5f024a0000000080bb4400989446006a60020028280000103d4780161649006a6102001e320000e43b47809c1549006a6202005e0a5e0098d046a01aa648006a63025454005e0040e745803cb747006a64020000005400e0764680844348006a6502140032000020994500337347006a66020a5e007200e0ab45003b8847006a6702001414000000c84400a89e46006a68021e1e1e000058184780b3f248006a69020000000000b06546002d3748006a6a02544a00680000964500a46e47006a6b02000a0a5e00108b4600585d48006a6c02000000000030404680071948006a6d020a4a004a00c05a4500362e47006a6e020a5e005e00207d46c0a74948006a6f020a54005400b001468031ce47006a7002004a004a00b03346c0a30e48006a7102540000000040674500443747006a72020000004a00904946c0bb1f48006a73020014140000e05d4680e02f48006a7402004a005400204b4680022148006a75020a00005400a00c460034df47006a76020a4a004a0040674500b23747006a7702004a0a4a0060384600531248006a78024a5e005e0098b74660519148006a79024a6800680040034500fcce46006a7a020028280000609f4500767b47006a7b02005e005e0070944640666a48006a7c02000a0a000000fa440010c546006a7d0200860186010000c04146c0341948006a7e02c6010a86010000400345004ecf46006a7f02001e1e000000614500d23147006a80020000000000401c450044f746006a8102005e005e0020fd45801ac847006a82020000000000504346c02c1a48006a8302140000000000fa4300a8c545006a84020054005400501146806ae547006a85020000000000409c4500ae7647006a86021414140000789b4640197648006a8702005400540060864500985447006a88020a4a004a0000964400546d46006a8902004a004a00803b45002a1447006a8a02000000000000000000000000006a8b02000a0a0000c0284500640547006a8c0200000a000080d4458014a847006a8d02000a0a000000c84300309e45006a8e020a14140000308e4680316148006a8f02000000000000164500f0ed46006a9002000000000000c84300a09e45006a9102000a0a000000af4400d68a46006a92024a0a0a000000964300006e45006a93024a0000000000c843ff9f9e45006a9402000000000000fa430048c645006a9502000000000000000000000000006a96024a0000000000964300c06d45006a97020054005400002f45008c0a47006a9802000000000000000000000000006a99020000000000002f4500780a47006a9a02004a004a00c0c14580349947006a9b020a00000000c04145004e1947006a9c024a0000000000964300306d45006a9d020a0000000080bb44005c9446006a9e020000000000f0524680e72648006a9f020000000000705f4680cb3048006aa002000000000000964300606d45006aa1024a0000000000fa4400a8c546006aa202004a004a0080d44580f8a747006aa3024a000a0000e0ab4500af8747006aa402000000000000af4400248a46006aa5024a0000000000164500a0ec46006aa602542828000080894680bf5848006aa7020068006800e0dd4500fbae47006aa8020a4a004a00f02046007ffd47006aa902000000540060b845001c9147006aaa024a0000000080d4440036a746006aab02000a0a000000964400346c46006aac024a00000000002f4400b40946006aad02000000000000000000000000006aae02000000000000fa4400b8c446006aaf02000a0a0000808945007c5847006ab002540000000000484400401d46006ab102000000000000964300e06b45006a0c03144a004a00601f4600d8fa47006a0d03000000000000000000000000006a0e03000a0a0000c0a84580dc8447006a0f03000000540000c84500759d47006a10030000000000c0a84500e48447006a110300540a5400e05d4640832e48006a12030000000000e0dd450073ae47006a13034a0000000060864500235347006a14030000004a0000614500bc3047006a15034a0a0a0000004846c0111d48006a1603000000000000af44007c8946006a17030a1414000080894400405846006a18035400000000d04f4680642348006a1903004a004a0020324600f10b48006a1a034a0a0a0000c08f4640b96148006a1b035400000000a0be4580859547006a1c030000000000007a4600184448006a1d03005400540020804500db4847006a1e03000000000000164500f0ea46006a1f030a4a004a00507546003e4048006a20030a00000000403546000e0e48006a21030a001e000080d44580c4a647006a22031e0000000000fa430090c445006a23035e1e1e000040354500490e47006a24031400000000e0924500546747006a2503000a0a0000103d4680e61448006a2603001e1e000000e14400a2b146006a27034a5400540000fa44004cc546006a2803001414000000964400986c46006a29034a0a0a680040034500d8ce46006a2a0300000a0000b8ba46e0689348006a2b03005400540000af4400188a46006a2c035e1e1e000080bb45008a9347006a2d035e0a0a0000004844004c1d46006a2e03001414000000c84300909d45006a2f030000140000c0da450085ac47006a30030014144a00802246800d0048006a3103000000000000c84300e09d45006a32030000000000404e4500cf2247006a3303004a004a00d01d46800ef947006a34030a14140000c0da4500e1ac47006a35030000004a0060d1458084a547006a3603004a004a0040b545804a8f47006a37034a14140000808944005c5946006a3803005400540000fa430088c545006a39031400004a0020e4458043b447006a3a03000000000000fa4400a8c546006a3b03004a004a000016450018ed46006a3c03000000000080224500600047006a3d03000000000020804500704a47006a3e03004a0a4a00806d4500a03b47006a3f03000000000000000000000000006a4003000000000000c84200e09d44006a4103005400540060064680e5d347006a42030000000000e0dd4580ddae47006a4303000000000000964400706c46006a44030a00000000408345000c4f47006a45030a00000000002f4500240a47006a46034a0000000000614400783146006a4703000000000000164400a0ec45006a48034a00000000704646c0641c48006a4903004a004a00c00f45007ce246006a4a03004a004a0040b54500ae8e47006a4b030000000000006145000c3147006a4c034a0a0a00004003460069ce47006a4d034a00000000404e45002a2247006a4e03000000000000964300e06b45006a4f03000a0a0000c05a45001f2c47006a50034a0000000000964300e06b45006a51030a00004a00c0734500c43f47006a5203000000000000af4400b48946006a5303000000000080ed4400e2ba46006a54030000000000c05a4500212c47006a55030000004a0000c844005e9d46006a5603000000000080224600bcff47006a57034a00004a00d01d468025f847006a58034a4a004a00e02b4600fb0648006a5903145e005e00e0dd46a03dae48006a5a030a0000000000484500001d47006a5b03000000000000964300806b45006a5c030a0a0a0000e0c44580c79a47006a5d0300000000008009450038d846006a5e030000000000100b4600adda47006a5f03000a0a0000a00c468032dd47006a60030000000000409c4500e67547006a61030a4a004a0000614400203146006a62030a0a0a0000c0da45805cac47006a63030014140000189246c07f6648006a64030a0a0a0000803b4500241447006a6503004a004a0080bb4400349446006a66030054005400a00c46000ede47006a6703000a0a0000609f4500817b47006a6803000000000000e144009cb146006a69034a00000000007a4400304546006a6a034a00000000c8c846a03d9e48006a6b03000a0a000010564600bf2848006a6c034a0a0a0000b01a4680e3f347006a6d030000000000007a4400304546006a6e034a0a0a0000803b4640e21348006a6f03000000000000af4400088a46006a7003000000000080d444009ca746006a71030000000000c08f4500c46247006a72030000004a00401c460074f647006a73034a000a0000e0924500866747006a7403000000000090494640db1e48006a7503000a0a000000af4400048a46006a76030000004a00100b46003edb47006a7703004a004a00002f4680f10948006a78030a4a004a0080a245802b8047006a79030a00000000c0da45008aac47006a7a03000000000000e1440078b146006a7b034a000a0000688d4600075f48006a7c030a00004a0010564600cd2848006a7d03005400540010244640560148006a7e0300000a000040834680de4e48006a7f030a00004a0018924680426648006a8003004a004a0070464640491c48006a8103000a0a0000ac0a47a093da48006a8203000000000000484400a01d46006a8303000000000000000000000000006a840300000000000c2d47f0610849')

data = binascii.unhexlify(b'004a1e543c023a4b11c53f4d') # b'5d03b0c101000a5400a82c4750c90549ff69')
                         #b'5e03000028000088db46c03caa48ff69'
                         #b'5f03281e1e5e0020644640963148ff69'
for i in range(len(data)):
    print(parseData(data[i:]))

print('\n\n')

for i in range(len(data)):
    print(parseData2(data[i:]))

print('\n\n')

for i in range(len(data) - 4):
    print(binascii.hexlify(data[i:i+4]), struct.unpack('f', data[i:i+4]))