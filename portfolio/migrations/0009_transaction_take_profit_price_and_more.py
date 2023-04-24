# Generated by Django 4.1.5 on 2023-04-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_transaction_buy_code_alter_transaction_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='take_profit_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='stock',
            field=models.CharField(blank=True, choices=[('AAA', 'AAA'), ('AAS', 'AAS'), ('AAT', 'AAT'), ('AAV', 'AAV'), ('ABB', 'ABB'), ('ABC', 'ABC'), ('ABS', 'ABS'), ('ACB', 'ACB'), ('ACL', 'ACL'), ('ACM', 'ACM'), ('ADS', 'ADS'), ('AFX', 'AFX'), ('AGF', 'AGF'), ('AGG', 'AGG'), ('AGM', 'AGM'), ('AGR', 'AGR'), ('AMS', 'AMS'), ('AMV', 'AMV'), ('ANV', 'ANV'), ('APG', 'APG'), ('APH', 'APH'), ('API', 'API'), ('APS', 'APS'), ('ASM', 'ASM'), ('ASP', 'ASP'), ('AST', 'AST'), ('ATA', 'ATA'), ('AVF', 'AVF'), ('B82', 'B82'), ('BAF', 'BAF'), ('BCA', 'BCA'), ('BCC', 'BCC'), ('BCE', 'BCE'), ('BCG', 'BCG'), ('BFC', 'BFC'), ('BIC', 'BIC'), ('BID', 'BID'), ('BIG', 'BIG'), ('BII', 'BII'), ('BKG', 'BKG'), ('BMI', 'BMI'), ('BMP', 'BMP'), ('BMS', 'BMS'), ('BNA', 'BNA'), ('BOT', 'BOT'), ('BSI', 'BSI'), ('BSR', 'BSR'), ('BVB', 'BVB'), ('BVG', 'BVG'), ('BVH', 'BVH'), ('BVS', 'BVS'), ('BWE', 'BWE'), ('C32', 'C32'), ('C4G', 'C4G'), ('C69', 'C69'), ('CBS', 'CBS'), ('CCL', 'CCL'), ('CDC', 'CDC'), ('CDO', 'CDO'), ('CEN', 'CEN'), ('CEO', 'CEO'), ('CHP', 'CHP'), ('CIG', 'CIG'), ('CII', 'CII'), ('CKG', 'CKG'), ('CLC', 'CLC'), ('CLG', 'CLG'), ('CLL', 'CLL'), ('CLX', 'CLX'), ('CMG', 'CMG'), ('CMX', 'CMX'), ('CNG', 'CNG'), ('CRE', 'CRE'), ('CSC', 'CSC'), ('CSI', 'CSI'), ('CST', 'CST'), ('CSV', 'CSV'), ('CTC', 'CTC'), ('CTD', 'CTD'), ('CTF', 'CTF'), ('CTG', 'CTG'), ('CTI', 'CTI'), ('CTR', 'CTR'), ('CTS', 'CTS'), ('CVN', 'CVN'), ('D2D', 'D2D'), ('DAG', 'DAG'), ('DAH', 'DAH'), ('DBC', 'DBC'), ('DBD', 'DBD'), ('DBT', 'DBT'), ('DCL', 'DCL'), ('DCM', 'DCM'), ('DCS', 'DCS'), ('DDG', 'DDG'), ('DDV', 'DDV'), ('DFF', 'DFF'), ('DGC', 'DGC'), ('DGW', 'DGW'), ('DHA', 'DHA'), ('DHC', 'DHC'), ('DHG', 'DHG'), ('DHM', 'DHM'), ('DHT', 'DHT'), ('DIC', 'DIC'), ('DID', 'DID'), ('DIG', 'DIG'), ('DIH', 'DIH'), ('DL1', 'DL1'), ('DLG', 'DLG'), ('DPG', 'DPG'), ('DPM', 'DPM'), ('DPR', 'DPR'), ('DPS', 'DPS'), ('DRC', 'DRC'), ('DRH', 'DRH'), ('DRI', 'DRI'), ('DSC', 'DSC'), ('DTD', 'DTD'), ('DTI', 'DTI'), ('DVG', 'DVG'), ('DVM', 'DVM'), ('DVN', 'DVN'), ('DVP', 'DVP'), ('DXG', 'DXG'), ('DXP', 'DXP'), ('DXS', 'DXS'), ('E1VFVN30', 'E1VFVN30'), ('EFI', 'EFI'), ('EIB', 'EIB'), ('ELC', 'ELC'), ('EVE', 'EVE'), ('EVF', 'EVF'), ('EVG', 'EVG'), ('EVS', 'EVS'), ('FCM', 'FCM'), ('FCN', 'FCN'), ('FID', 'FID'), ('FIR', 'FIR'), ('FIT', 'FIT'), ('FMC', 'FMC'), ('FPT', 'FPT'), ('FRT', 'FRT'), ('FTM', 'FTM'), ('FTS', 'FTS'), ('FUEDCMID', 'FUEDCMID'), ('FUEKIV30', 'FUEKIV30'), ('FUEKIVFS', 'FUEKIVFS'), ('FUEMAV30', 'FUEMAV30'), ('FUEVFVND', 'FUEVFVND'), ('FUEVN100', 'FUEVN100'), ('G20', 'G20'), ('G36', 'G36'), ('GAS', 'GAS'), ('GDT', 'GDT'), ('GEG', 'GEG'), ('GEX', 'GEX'), ('GIL', 'GIL'), ('GKM', 'GKM'), ('GMC', 'GMC'), ('GMD', 'GMD'), ('GMX', 'GMX'), ('GSP', 'GSP'), ('GTT', 'GTT'), ('GVR', 'GVR'), ('HAG', 'HAG'), ('HAH', 'HAH'), ('HAP', 'HAP'), ('HAR', 'HAR'), ('HAX', 'HAX'), ('HBC', 'HBC'), ('HBS', 'HBS'), ('HCD', 'HCD'), ('HCM', 'HCM'), ('HD2', 'HD2'), ('HDA', 'HDA'), ('HDB', 'HDB'), ('HDC', 'HDC'), ('HDG', 'HDG'), ('HHG', 'HHG'), ('HHP', 'HHP'), ('HHS', 'HHS'), ('HHV', 'HHV'), ('HID', 'HID'), ('HII', 'HII'), ('HKB', 'HKB'), ('HLA', 'HLA'), ('HLC', 'HLC'), ('HLD', 'HLD'), ('HMS', 'HMS'), ('HNG', 'HNG'), ('HNM', 'HNM'), ('HPG', 'HPG'), ('HPX', 'HPX'), ('HQC', 'HQC'), ('HSG', 'HSG'), ('HSL', 'HSL'), ('HT1', 'HT1'), ('HTN', 'HTN'), ('HTT', 'HTT'), ('HUT', 'HUT'), ('HVA', 'HVA'), ('HVH', 'HVH'), ('HVN', 'HVN'), ('IBC', 'IBC'), ('IDC', 'IDC'), ('IDI', 'IDI'), ('IDJ', 'IDJ'), ('IJC', 'IJC'), ('ILA', 'ILA'), ('IMP', 'IMP'), ('IPA', 'IPA'), ('ITA', 'ITA'), ('ITC', 'ITC'), ('ITD', 'ITD'), ('ITQ', 'ITQ'), ('ITS', 'ITS'), ('IVS', 'IVS'), ('JVC', 'JVC'), ('KBC', 'KBC'), ('KDC', 'KDC'), ('KDH', 'KDH'), ('KHG', 'KHG'), ('KHL', 'KHL'), ('KHP', 'KHP'), ('KLB', 'KLB'), ('KMR', 'KMR'), ('KOS', 'KOS'), ('KPF', 'KPF'), ('KSB', 'KSB'), ('KSD', 'KSD'), ('KSH', 'KSH'), ('KSQ', 'KSQ'), ('KTS', 'KTS'), ('KTT', 'KTT'), ('KVC', 'KVC'), ('L14', 'L14'), ('L18', 'L18'), ('L44', 'L44'), ('LAS', 'LAS'), ('LCG', 'LCG'), ('LCM', 'LCM'), ('LDG', 'LDG'), ('LDP', 'LDP'), ('LHG', 'LHG'), ('LIC', 'LIC'), ('LIG', 'LIG'), ('LMH', 'LMH'), ('LPB', 'LPB'), ('LSS', 'LSS'), ('LTC', 'LTC'), ('LTG', 'LTG'), ('MBB', 'MBB'), ('MBG', 'MBG'), ('MBS', 'MBS'), ('MCG', 'MCG'), ('MDC', 'MDC'), ('MIG', 'MIG'), ('MPC', 'MPC'), ('MPT', 'MPT'), ('MSB', 'MSB'), ('MSH', 'MSH'), ('MSN', 'MSN'), ('MSR', 'MSR'), ('MST', 'MST'), ('MTL', 'MTL'), ('MWG', 'MWG'), ('NAB', 'NAB'), ('NAF', 'NAF'), ('NAG', 'NAG'), ('NBB', 'NBB'), ('NBC', 'NBC'), ('NCT', 'NCT'), ('NDN', 'NDN'), ('NDX', 'NDX'), ('NED', 'NED'), ('NHA', 'NHA'), ('NHH', 'NHH'), ('NHP', 'NHP'), ('NHV', 'NHV'), ('NKG', 'NKG'), ('NLG', 'NLG'), ('NRC', 'NRC'), ('NSC', 'NSC'), ('NSH', 'NSH'), ('NT2', 'NT2'), ('NTB', 'NTB'), ('NTL', 'NTL'), ('NTP', 'NTP'), ('NVB', 'NVB'), ('NVL', 'NVL'), ('OCB', 'OCB'), ('OCH', 'OCH'), ('ODE', 'ODE'), ('OGC', 'OGC'), ('OIL', 'OIL'), ('ONE', 'ONE'), ('ORS', 'ORS'), ('PAN', 'PAN'), ('PAS', 'PAS'), ('PBC', 'PBC'), ('PC1', 'PC1'), ('PCH', 'PCH'), ('PDR', 'PDR'), ('PDV', 'PDV'), ('PET', 'PET'), ('PFL', 'PFL'), ('PGB', 'PGB'), ('PGN', 'PGN'), ('PHC', 'PHC'), ('PHR', 'PHR'), ('PIV', 'PIV'), ('PLC', 'PLC'), ('PLP', 'PLP'), ('PLX', 'PLX'), ('PNJ', 'PNJ'), ('POM', 'POM'), ('POW', 'POW'), ('PPC', 'PPC'), ('PPI', 'PPI'), ('PPT', 'PPT'), ('PSD', 'PSD'), ('PSH', 'PSH'), ('PSI', 'PSI'), ('PTB', 'PTB'), ('PTC', 'PTC'), ('PTL', 'PTL'), ('PV2', 'PV2'), ('PVA', 'PVA'), ('PVB', 'PVB'), ('PVC', 'PVC'), ('PVD', 'PVD'), ('PVE', 'PVE'), ('PVG', 'PVG'), ('PVI', 'PVI'), ('PVP', 'PVP'), ('PVS', 'PVS'), ('PVT', 'PVT'), ('PVX', 'PVX'), ('PXI', 'PXI'), ('PXL', 'PXL'), ('PXS', 'PXS'), ('PXT', 'PXT'), ('QBS', 'QBS'), ('QCG', 'QCG'), ('QNS', 'QNS'), ('QTP', 'QTP'), ('RAL', 'RAL'), ('RDP', 'RDP'), ('REE', 'REE'), ('RGC', 'RGC'), ('S96', 'S96'), ('S99', 'S99'), ('SAB', 'SAB'), ('SAM', 'SAM'), ('SBS', 'SBS'), ('SBT', 'SBT'), ('SCG', 'SCG'), ('SCI', 'SCI'), ('SCR', 'SCR'), ('SCS', 'SCS'), ('SDA', 'SDA'), ('SDD', 'SDD'), ('SDP', 'SDP'), ('SEA', 'SEA'), ('SFI', 'SFI'), ('SGP', 'SGP'), ('SGR', 'SGR'), ('SGT', 'SGT'), ('SHA', 'SHA'), ('SHB', 'SHB'), ('SHI', 'SHI'), ('SHP', 'SHP'), ('SHS', 'SHS'), ('SIP', 'SIP'), ('SJF', 'SJF'), ('SJS', 'SJS'), ('SKG', 'SKG'), ('SLS', 'SLS'), ('SMC', 'SMC'), ('SPI', 'SPI'), ('SRA', 'SRA'), ('SSB', 'SSB'), ('SSH', 'SSH'), ('SSI', 'SSI'), ('SSN', 'SSN'), ('ST8', 'ST8'), ('STB', 'STB'), ('STG', 'STG'), ('STH', 'STH'), ('STK', 'STK'), ('SZC', 'SZC'), ('TAR', 'TAR'), ('TC6', 'TC6'), ('TCB', 'TCB'), ('TCD', 'TCD'), ('TCH', 'TCH'), ('TCI', 'TCI'), ('TCM', 'TCM'), ('TCO', 'TCO'), ('TCT', 'TCT'), ('TDC', 'TDC'), ('TDG', 'TDG'), ('TDH', 'TDH'), ('TDM', 'TDM'), ('TDN', 'TDN'), ('TEG', 'TEG'), ('TGG', 'TGG'), ('THG', 'THG'), ('THT', 'THT'), ('TID', 'TID'), ('TIG', 'TIG'), ('TIP', 'TIP'), ('TKC', 'TKC'), ('TLD', 'TLD'), ('TLG', 'TLG'), ('TLH', 'TLH'), ('TNA', 'TNA'), ('TNG', 'TNG'), ('TNH', 'TNH'), ('TNI', 'TNI'), ('TNS', 'TNS'), ('TNT', 'TNT'), ('TOP', 'TOP'), ('TPB', 'TPB'), ('TSC', 'TSC'), ('TTA', 'TTA'), ('TTB', 'TTB'), ('TTF', 'TTF'), ('TTH', 'TTH'), ('TV2', 'TV2'), ('TV4', 'TV4'), ('TV6', 'TV6'), ('TVB', 'TVB'), ('TVC', 'TVC'), ('TVD', 'TVD'), ('TVN', 'TVN'), ('UDC', 'UDC'), ('V11', 'V11'), ('VAB', 'VAB'), ('VC3', 'VC3'), ('VC7', 'VC7'), ('VCB', 'VCB'), ('VCG', 'VCG'), ('VCI', 'VCI'), ('VCR', 'VCR'), ('VCS', 'VCS'), ('VDS', 'VDS'), ('VE9', 'VE9'), ('VEA', 'VEA'), ('VFS', 'VFS'), ('VGC', 'VGC'), ('VGI', 'VGI'), ('VGS', 'VGS'), ('VGT', 'VGT'), ('VGV', 'VGV'), ('VHC', 'VHC'), ('VHE', 'VHE'), ('VHG', 'VHG'), ('VHM', 'VHM'), ('VIB', 'VIB'), ('VIC', 'VIC'), ('VID', 'VID'), ('VIG', 'VIG'), ('VIP', 'VIP'), ('VIX', 'VIX'), ('VJC', 'VJC'), ('VKC', 'VKC'), ('VLB', 'VLB'), ('VLC', 'VLC'), ('VLF', 'VLF'), ('VNB', 'VNB'), ('VND', 'VND'), ('VNE', 'VNE'), ('VNH', 'VNH'), ('VNL', 'VNL'), ('VNM', 'VNM'), ('VNP', 'VNP'), ('VNR', 'VNR'), ('VNS', 'VNS'), ('VOC', 'VOC'), ('VOS', 'VOS'), ('VPB', 'VPB'), ('VPG', 'VPG'), ('VPH', 'VPH'), ('VPI', 'VPI'), ('VRC', 'VRC'), ('VRE', 'VRE'), ('VSC', 'VSC'), ('VSH', 'VSH'), ('VST', 'VST'), ('VTD', 'VTD'), ('VTO', 'VTO'), ('VTP', 'VTP'), ('VTR', 'VTR'), ('VTZ', 'VTZ'), ('VUA', 'VUA'), ('WSS', 'WSS'), ('YEG', 'YEG'), ('YTC', 'YTC')], max_length=8, null=True),
        ),
    ]
