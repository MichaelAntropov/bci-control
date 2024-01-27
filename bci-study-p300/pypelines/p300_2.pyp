<?xml version='1.0' encoding='utf-8'?>
<scheme version="2.0" title="pipeline" description="">
	<nodes>
		<node id="0" name="Import XDF" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" project_name="NeuroPype" version="1.4.3" title="Import XDF" uuid="e119a910-c526-4959-b9f1-0c4c2b56a7ab" position="(292.0, 293.0)" />
		<node id="1" name="Scrolling Plot (Offline)" qualified_name="widgets.visualization.owscrollplot.OWScrollPlot" project_name="NeuroPype" version="1.0.1" title="Scrolling Plot (Offline)" uuid="5759401b-e8c5-417b-bef1-9404c928586f" position="(758.5290758827948, 386.61036814425245)" />
		<node id="2" name="Extract Streams" qualified_name="widgets.formatting.owextractstreams.OWExtractStreams" project_name="NeuroPype" version="2.2.1" title="Extract Streams" uuid="04a2a5be-fe9c-45fe-9fe4-3d729ed4e496" position="(446.0, 346.0)" />
		<node id="3" name="Extract Streams" qualified_name="widgets.formatting.owextractstreams.OWExtractStreams" project_name="NeuroPype" version="2.2.1" title="Extract Streams" uuid="5dfacacf-d8d5-4150-ad83-188aa8649c7c" position="(406.0, 203.0)" />
		<node id="4" name="Set Axis Values" qualified_name="widgets.tensor_math.owsetaxisvalues.OWSetAxisValues" project_name="NeuroPype" version="0.2.0" title="Set Axis Values" uuid="2351137e-491a-4dc1-9415-957355a5cc09" position="(528.0, 203.0)" />
		<node id="5" name="Merge Streams" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" project_name="NeuroPype" version="1.0.0" title="Merge Streams" uuid="4826f7a4-66b0-491b-ac8c-105422d1aa3f" position="(626.0, 267.0)" />
		<node id="6" name="Preprocess EEG (Meta)" qualified_name="widgets.neural.owpreprocesseeg.OWPreprocessEEG" project_name="NeuroPype" version="1.2.2" title="PreprocessEEG (Meta)" uuid="d3cfa5e2-9e4f-4a31-be67-2438e28e6357" position="(814.4740796393687, 272.58677685950414)" />
		<node id="7" name="Insert Markers" qualified_name="widgets.markers.owinsertmarkers.OWInsertMarkers" project_name="NeuroPype" version="1.2.0" title="Insert Markers (stim correct)" uuid="a578036d-eb84-4e49-a75b-7648f4c74aba" position="(644.1735537190082, -83.30578512396679)" />
		<node id="8" name="Insert Markers" qualified_name="widgets.markers.owinsertmarkers.OWInsertMarkers" project_name="NeuroPype" version="1.2.0" title="Insert Markers (stim incorrect)" uuid="d794b196-cbf3-4e8f-a49c-be674ac3da18" position="(750.9999999999998, -83.47933884297524)" />
		<node id="9" name="Event Related Potential (Meta)" qualified_name="widgets.neural.oweventrelatedpotential.OWEventRelatedPotential" project_name="NeuroPype" version="1.0.2" title="Event Related Potential (Meta)" uuid="4acd7f3a-82aa-46fa-a4a9-ab9c10fb5cc4" position="(1084.3801652892566, 307.52066115702485)" />
		<node id="10" name="Grouped Mean" qualified_name="widgets.statistics.owgroupedmean.OWGroupedMean" project_name="NeuroPype" version="1.1.0" title="Grouped Mean" uuid="1e576fdf-fb23-45e1-8af0-e95f9497e998" position="(1214.3966942148759, 314.87603305785126)" />
		<node id="11" name="Set Stream Properties" qualified_name="widgets.utilities.owsetstreamproperties.OWSetStreamProperties" project_name="NeuroPype" version="1.3.2" title="Set Stream Properties" uuid="573b1fb7-118a-4849-a24a-518cf4dfa4a8" position="(1342.97520661157, 325.6198347107439)" />
		<node id="12" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Filter Channels (midline)" uuid="389df5fe-e147-443f-89ee-9089669bcd2e" position="(1553.0661157024792, 368.42148760330576)" />
		<node id="13" name="Select Instances" qualified_name="widgets.formatting.owselectinstances.OWSelectInstances" project_name="NeuroPype" version="1.1.1" title="Select correct" uuid="4e8171a2-955c-4717-832d-154540730545" position="(1452.0661157024792, 269.42148760330576)" />
		<node id="14" name="Time Series Plot" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" project_name="NeuroPype" version="1.2.0" title="Time Series Plot" uuid="b193df2d-a085-421c-bbb3-3a632aa494c3" position="(1750.157024793388, 368.42148760330576)" />
		<node id="15" name="Time Series Plot" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" project_name="NeuroPype" version="1.2.0" title="Time Series Plot" uuid="c0e74cce-5cd7-4391-9303-0e4791b4c583" position="(1751.2396694214879, 269.42148760330576)" />
		<node id="16" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Filter Channels (midline)" uuid="b7b9762b-ef09-452e-84b4-39e95f4106cd" position="(1552.0661157024792, 269.42148760330576)" />
		<node id="17" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Select Range" uuid="006ff5cb-e95d-4c37-ad46-9f8766acd5fe" position="(1650.0661157024792, 370.42148760330576)" />
		<node id="18" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Select Range" uuid="825f9d5f-eb2c-45c5-a587-7f90e6497c6c" position="(1653.8842975206612, 269.4214876033057)" />
		<node id="19" name="Select Instances" qualified_name="widgets.formatting.owselectinstances.OWSelectInstances" project_name="NeuroPype" version="1.1.1" title="Select incorrect" uuid="912fb384-34af-4671-b44b-89dd85f41462" position="(1452.0661157024792, 369.42148760330576)" />
		<node id="20" name="Assign Target Values" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" project_name="NeuroPype" version="1.0.1" title="Assign Target Values" uuid="824e4a10-7e34-426d-8437-be7ba3a8be8d" position="(941.4049586776857, 287.47933884297515)" />
		<node id="21" name="Inspect Packet" qualified_name="widgets.visualization.owinspectpacket.OWInspectPacket" project_name="NeuroPype" version="3.0.1" title="Inspect Packet" uuid="f261ca3d-1395-4ed6-8bbf-7729767f8d79" position="(751.7355371900828, 124.01652892561978)" />
		<node id="22" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Filter Channels (midline)" uuid="a09c741b-868c-4409-bb18-e774ef155238" position="(1553.9752066115705, 463.87603305785126)" />
		<node id="23" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Select Range" uuid="0886f5c4-ea47-4655-8e9f-8373d33ddc8f" position="(1650.9752066115705, 465.87603305785126)" />
		<node id="24" name="Time Series Plot" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" project_name="NeuroPype" version="1.2.0" title="Time Series Plot" uuid="d14fded6-a86a-49c5-850f-a83bc139ef87" position="(1751.066115702479, 463.87603305785126)" />
		<node id="25" name="Select Instances" qualified_name="widgets.formatting.owselectinstances.OWSelectInstances" project_name="NeuroPype" version="1.1.1" title="Select incorrect" uuid="50c01cbf-5037-4bb3-8e55-457c4e6e451e" position="(1452.9752066115705, 464.87603305785126)" />
	</nodes>
	<links>
		<link id="0" source_node_id="0" sink_node_id="3" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="1" source_node_id="0" sink_node_id="2" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="2" source_node_id="3" sink_node_id="4" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="3" source_node_id="4" sink_node_id="5" source_channel="Data" sink_channel="Data1" enabled="true" />
		<link id="4" source_node_id="2" sink_node_id="5" source_channel="Data" sink_channel="Data2" enabled="true" />
		<link id="5" source_node_id="5" sink_node_id="6" source_channel="Outdata" sink_channel="Data" enabled="true" />
		<link id="6" source_node_id="9" sink_node_id="10" source_channel="Erp Data" sink_channel="Data" enabled="true" />
		<link id="7" source_node_id="10" sink_node_id="11" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="8" source_node_id="19" sink_node_id="12" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="9" source_node_id="12" sink_node_id="17" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="10" source_node_id="13" sink_node_id="16" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="11" source_node_id="17" sink_node_id="14" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="12" source_node_id="18" sink_node_id="15" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="13" source_node_id="16" sink_node_id="18" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="14" source_node_id="11" sink_node_id="13" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="15" source_node_id="11" sink_node_id="19" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="16" source_node_id="20" sink_node_id="9" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="17" source_node_id="6" sink_node_id="20" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="18" source_node_id="25" sink_node_id="22" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="19" source_node_id="22" sink_node_id="23" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="20" source_node_id="23" sink_node_id="24" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="21" source_node_id="11" sink_node_id="25" source_channel="Data" sink_channel="Data" enabled="true" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties node_id="0" format="pickle">gASVHAIAAAAAAAB9lCiMDWNsb3VkX2FjY291bnSUjACUjAxjbG91ZF9idWNrZXSUaAKMEWNsb3Vk
X2NyZWRlbnRpYWxzlGgCjApjbG91ZF9ob3N0lIwHRGVmYXVsdJSMCGZpbGVuYW1llIxHQzovcmVj
b3JkaW5ncy9wMzAwXzIveWVnb3Jfay8zL3llZ29yX2tfcDMwMF8yXzIwMjQtMDEtMjdfMTktNTUt
MDRfMy54ZGaUjBNoYW5kbGVfY2xvY2tfcmVzZXRzlIiMEWhhbmRsZV9jbG9ja19zeW5jlIiMFWhh
bmRsZV9qaXR0ZXJfcmVtb3ZhbJSIjA5tYXhfbWFya2VyX2xlbpSMDSh1c2UgZGVmYXVsdCmUjAht
ZXRhZGF0YZR9lIwScmVvcmRlcl90aW1lc3RhbXBzlImMDnJldGFpbl9zdHJlYW1zlGgNjBNzYXZl
ZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSM
ClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAwsAAAF6AAAEdAAAAngAAAMMAAABmQAABHMAAAJ3AAAA
AAAAAAAHgAAAAwwAAAGZAAAEcwAAAneUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAt1c2VfY2Fj
aGluZ5SJjA91c2Vfc3RyZWFtbmFtZXOUiYwHdmVyYm9zZZSJdS4=
</properties>
		<properties node_id="1" format="pickle">gASVVwIAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiYwLYW50aWFsaWFzZWSUiIwJYXV0b3NjYWxl
lIiMEGJhY2tncm91bmRfY29sb3KUjAcjRkZGRkZGlIwQZGVjb3JhdGlvbl9jb2xvcpSMByMwMDAw
MDCUjAtkb3duc2FtcGxlZJSJjAxpbml0aWFsX2RpbXOUXZQoSzJLMk28Ak30AWWMCmxpbmVfY29s
b3KUjAcjMDAwMDAwlIwKbGluZV93aWR0aJRHP+gAAAAAAACMDG1hcmtlcl9jb2xvcpSMByNGRjAw
MDCUjAhtZXRhZGF0YZR9lIwMbmFuc19hc196ZXJvlImMDm92ZXJyaWRlX3NyYXRllIwNKHVzZSBk
ZWZhdWx0KZSMDHBsb3RfbWFya2Vyc5SIjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3Vu
cGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAwsA
AAFRAAAEdAAAAqAAAAMMAAABcAAABHMAAAKfAAAAAAAAAAAHgAAAAwwAAAFwAAAEcwAAAp+UhZSH
lFKUjAVzY2FsZZRHP8mZmZmZmZqMDnNldF9icmVha3BvaW50lImMC3N0cmVhbV9uYW1llIwNKHVz
ZSBkZWZhdWx0KZSMCnRpbWVfcmFuZ2WUR0AUAAAAAAAAjAV0aXRsZZSMEFRpbWUgc2VyaWVzIHZp
ZXeUjAp6ZXJvX2NvbG9ylIwHIzdGN0Y3RpSMCHplcm9tZWFulIh1Lg==
</properties>
		<properties node_id="2" format="pickle">gASVDQEAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwO
X3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAA
AwsAAAGVAAAEdAAAAl0AAAMMAAABtAAABHMAAAJcAAAAAAAAAAAHgAAAAwwAAAG0AAAEcwAAAlyU
hZSHlFKUjBJzZWxlY3Rpb25fY3JpdGVyaWGUfZSMDnNldF9icmVha3BvaW50lImMDHN0cmVhbV9u
YW1lc5RdlIwHbWFya2Vyc5RhjBFzdXBwb3J0X3dpbGRjYXJkc5SJjAd2ZXJib3NllIl1Lg==
</properties>
		<properties node_id="3" format="pickle">gASVCQEAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwO
X3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAA
AwsAAAGVAAAEdAAAAl0AAAMMAAABtAAABHMAAAJcAAAAAAAAAAAHgAAAAwwAAAG0AAAEcwAAAlyU
hZSHlFKUjBJzZWxlY3Rpb25fY3JpdGVyaWGUfZSMDnNldF9icmVha3BvaW50lImMDHN0cmVhbV9u
YW1lc5RdlIwDZWVnlGGMEXN1cHBvcnRfd2lsZGNhcmRzlImMB3ZlcmJvc2WUiXUu
</properties>
		<properties node_id="4" format="pickle">gASVqgEAAAAAAAB9lCiMCmFycmF5X25hbWWUjA0odXNlIGRlZmF1bHQplIwEYXhpc5SMBXNwYWNl
lIwKYXhpc19sYWJlbJSMDSh1c2UgZGVmYXVsdCmUjA9heGlzX29jY3VycmVuY2WUSwCMD2hhbmRs
ZV9leGlzdGluZ5SMC3JlcGxhY2UtYWxslIwIbWV0YWRhdGGUfZSMDG9ubHlfc2lnbmFsc5SIjBNz
YXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29y
ZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAABA0AAAFJAAAFdgAAAhcAAAQOAAABaAAABXUAAAIW
AAAAAAAAAAAHgAAABA4AAAFoAAAFdQAAAhaUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAZ2YWx1
ZXOUXZQojANmcDGUjANmcDKUjANwbzOUjANwbzSUjAJwN5SMAnA4lIwDcG81lIwDcG82lIwCZjeU
jAJmOJSMAkN6lIwCRnqUjAJQepSMAk96lIwCcDOUjAJwNJRldS4=
</properties>
		<properties node_id="5" format="pickle">gASV4QAAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjBFyZXBsYWNlX2lmX2V4aXN0c5SJjBNzYXZlZFdp
ZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFC
eXRlQXJyYXmUQ0IB2dDLAAMAAAAAAwsAAAGrAAAEdAAAAkYAAAMMAAABygAABHMAAAJFAAAAAAAA
AAAHgAAAAwwAAAHKAAAEcwAAAkWUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAdzb3J0aW5nlIwF
aW5wdXSUdS4=
</properties>
		<properties node_id="6" format="pickle">gASVFAQAAAAAAAB9lCiMGmJhZF9jaGFubmVsX2NvcnJfdGhyZXNob2xklEc/5mZmZmZmZowbYmFk
X2NoYW5uZWxfbWF4X2Jyb2tlbl90aW1llEc/2ZmZmZmZmowbYmFkX2NoYW5uZWxfbm9pc2VfdGhy
ZXNob2xklEsEjBdiYWRfd2luZG93X3JlbW92YWxfYmFuZJRdlIwUYnVyc3RfcmVtb3ZhbF9jdXRv
ZmaUR0AkAAAAAAAAjA1jYWxpYl9zZWNvbmRzlEsAjBJjaGFubmVsc190b19pbXBvcnSUjANhbGyU
jBJjbGVhbl9zaWduYWxfcmFuZ2WUXZQoSvz///9LBmWMDGRlc2lyZWRfdW5pdJSMAnVWlIwMZXhw
b3J0X3RvX2g1lImMD2V4dHJhX2FyX3BhcmFtc5R9lIwIZml4X3VuaXSUiIwUaGlnaHBhc3NfZnJl
cXVlbmNpZXOUXZQoRz+5mZmZmZmaRz/JmZmZmZmaZYwTaGlnaHBhc3Nfc3RvcF9hdHRlbpRHQEkA
AAAAAACMB2luaXRfb26UXZSME2xvd3Bhc3NfZnJlcXVlbmNpZXOUXZQoSw9LEGWMEmxvd3Bhc3Nf
c3RvcF9hdHRlbpRLUIwQbWF4X2JhZF9jaGFubmVsc5RHP8mZmZmZmZqMD21heF9icm9rZW5fdGlt
ZZRHP9mZmZmZmZqMCG1ldGFkYXRhlH2UjAdtb250YWdllIwEYXV0b5SMD25vdGNoX2ZyZXF1ZW5j
eZRHQEkAAAAAAACMC251bV9zYW1wbGVzlE1eAYwicHJvdGVjdGVkX2NoYW5uZWxzX2R1cmluZ19j
bGVhbmluZ5RdlIwYcmVtb3ZlX3VubG9jYWxpemVkX2NoYW5zlIiMDXJlcmVmZXJlbmNpbmeUjAND
QVKUjA1zYW1wbGluZ19yYXRllIwNKHVzZSBkZWZhdWx0KZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmU
jANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ
0MsAAwAAAAADBgAAAIEAAAR5AAADcAAAAwcAAACgAAAEeAAAA28AAAAAAAAAAAeAAAADBwAAAKAA
AAR4AAADb5SFlIeUUpSMDHNjYWxlX2ZhY3RvcpRHP/AAAAAAAACMDnNldF9icmVha3BvaW50lImM
EHNraXBfaW50ZXJwb2xhdGWUiYwSc2tpcF9wcmVwcm9jZXNzaW5nlImMC3N1YnNldF9zaXpllEc/
yZmZmZmZmowLdXNlX2NhY2hpbmeUiIwQdXNlX2NsZWFuX3dpbmRvd5SIjBB1c2Vfbm90Y2hfZmls
dGVylImMCndpbmRvd19sZW6URz/gAAAAAAAAdS4=
</properties>
		<properties node_id="7" format="pickle">gASVigIAAAAAAAB9lCiMDWFuY2hvcl9tYXJrZXKUjBQnc3RpbXVsdXMnIGluIE1hcmtlcpSMD2Fu
Y2hvcl9tYXJrZXJfQpSMHk1hcmtlcj09J3Jlc3BvbnNlLXdhcy1jb3JyZWN0J5SMBWNvdW50lEsB
jAhjb3VudGluZ5SMC3BlcmludGVydmFslIwXZW5mb3JjZV9pbnRlcm1pdHRlbnRfaW6UjAttYXJr
ZXItc3BhbpSMDmV4Y2VwdF9tYXJrZXJzlF2UjAxleHRyYV9saW1pdHOUXZSMFGluc3RhbmNlX2Zp
ZWxkc19mcm9tlIwFZmlyc3SUjBRpbnRlcm1pdHRlbnRfbWFya2Vyc5SMBWFsbG93lIwNbWFya2Vy
X2Zvcm1hdJSMCmNvbmRpdGlvbnOUjAptYXhfbGVuZ3RolIwNKHVzZSBkZWZhdWx0KZSMCG1ldGFk
YXRhlH2UjAptaW5fbGVuZ3RolIwNKHVzZSBkZWZhdWx0KZSMBG1vZGWUjA5tYXJrZXItc3Bhbm5l
ZJSMB3BheWxvYWSUjAxzdGltLWNvcnJlY3SUjAlwbGFjZW1lbnSUjAtlcXVpZGlzdGFudJSMC3Jh
bmRvbV9zZWVklE05MIwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBl
lJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAALyAAAA9gAABI4AAAL8
AAAC8wAAARUAAASNAAAC+wAAAAAAAAAAB4AAAALzAAABFQAABI0AAAL7lIWUh5RSlIwOc2V0X2Jy
ZWFrcG9pbnSUiYwLdGltZV9saW1pdHOUXZQoSwBLAGV1Lg==
</properties>
		<properties node_id="8" format="pickle">gASVjgIAAAAAAAB9lCiMDWFuY2hvcl9tYXJrZXKUjBQnc3RpbXVsdXMnIGluIE1hcmtlcpSMD2Fu
Y2hvcl9tYXJrZXJfQpSMIE1hcmtlcj09J3Jlc3BvbnNlLXdhcy1pbmNvcnJlY3QnlIwFY291bnSU
SwGMCGNvdW50aW5nlIwLcGVyaW50ZXJ2YWyUjBdlbmZvcmNlX2ludGVybWl0dGVudF9pbpSMC21h
cmtlci1zcGFulIwOZXhjZXB0X21hcmtlcnOUXZSMDGV4dHJhX2xpbWl0c5RdlIwUaW5zdGFuY2Vf
ZmllbGRzX2Zyb22UjAVmaXJzdJSMFGludGVybWl0dGVudF9tYXJrZXJzlIwFYWxsb3eUjA1tYXJr
ZXJfZm9ybWF0lIwKY29uZGl0aW9uc5SMCm1heF9sZW5ndGiUjA0odXNlIGRlZmF1bHQplIwIbWV0
YWRhdGGUfZSMCm1pbl9sZW5ndGiUjA0odXNlIGRlZmF1bHQplIwEbW9kZZSMDm1hcmtlci1zcGFu
bmVklIwHcGF5bG9hZJSMDnN0aW0taW5jb3JyZWN0lIwJcGxhY2VtZW50lIwLZXF1aWRpc3RhbnSU
jAtyYW5kb21fc2VlZJRNOTCME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVf
dHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAAC8gAAAPYAAASO
AAAC/AAAAvMAAAEVAAAEjQAAAvsAAAAAAAAAAAeAAAAC8wAAARUAAASNAAAC+5SFlIeUUpSMDnNl
dF9icmVha3BvaW50lImMC3RpbWVfbGltaXRzlF2UKEsASwBldS4=
</properties>
		<properties node_id="9" format="pickle">gASVbwEAAAAAAAB9lCiMFmJhc2VsaW5lX3JlbW92YWxfcmFuZ2WUjAgtMC4zLi4uMJSMDWNoYW5u
ZWxfcmFuZ2WUjAE6lIwObG93cGFzc19jdXRvZmaUXZSMDm1heF9nYXBfbGVuZ3RolEc/yZmZmZmZ
mowIbWV0YWRhdGGUfZSMDm91dHB1dF9tZWFzdXJllIwGdHJpYWxzlIwTc2F2ZWRXaWRnZXRHZW9t
ZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFycmF5
lENCAdnQywADAAAAAAL8AAABKgAABGUAAAJdAAAC/QAAAUkAAARkAAACXAAAAAAAAAAAB4AAAAL9
AAABSQAABGQAAAJclIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwVc2tpcF9iYXNlbGluZV9yZW1v
dmFslImMC3RpbWVfYm91bmRzlF2UKEe/0zMzMzMzM0sBZXUu
</properties>
		<properties node_id="10" format="pickle">gASVkQEAAAAAAAB9lCiMDWFsbG93X21hcmtlcnOUiYwIY2lfcmFuZ2WURz/uZmZmZmZmjARkZG9m
lEsBjAllcXVhbF92YXKUiYwKZXJyb3JfdHlwZZSMBG5vbmWUjAlmaWxsX2NvbHOUiIwKZ3JvdXBf
Y29sc5RdlIwGTWFya2VylGGMDWdyb3VwaW5nX3R5cGWUjAZsZXZlbHOUjAltZWFuX3R5cGWUjARt
ZWFulIwIbWV0YWRhdGGUfZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVf
dHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAADCwAAAX0AAAR0
AAACdQAAAwwAAAGcAAAEcwAAAnQAAAAAAAAAAAeAAAADDAAAAZwAAARzAAACdJSFlIeUUpSMDnNl
dF9icmVha3BvaW50lImMD3RyaW1fcHJvcG9ydGlvbpRdlChLAEsAZYwLdXNlX2NhY2hpbmeUiYwJ
d2luc29yaXpllIl1Lg==
</properties>
		<properties node_id="11" format="pickle">gASVBwEAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjAxvbmx5X3NpZ25hbHOUiYwKcHJvcGVydGllc5R9
lIwLaGFzX21hcmtlcnOUiXOME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVf
dHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAADCwAAAaoAAAR0
AAACSAAAAwwAAAHJAAAEcwAAAkcAAAAAAAAAAAeAAAADDAAAAckAAARzAAACR5SFlIeUUpSMDnNl
dF9icmVha3BvaW50lImMC3N0cmVhbV9uYW1llIwNKHVzZSBkZWZhdWx0KZR1Lg==
</properties>
		<properties node_id="12" format="pickle">gASVNgEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwFc3BhY2WUjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAAMLAAABkwAABHQAAAJeAAADDAAAAbIAAARzAAACXQAAAAAAAAAAB4AA
AAMMAAABsgAABHMAAAJdlIWUh5RSlIwJc2VsZWN0aW9ulF2UKIwCRnqUjAJDepSMAlB6lIwCT3qU
ZYwOc2V0X2JyZWFrcG9pbnSUiYwEdW5pdJSMBW5hbWVzlHUu
</properties>
		<properties node_id="13" format="pickle">gASVnwEAAAAAAAB9lCiME2Fzc2lnbl90YXJnZXRfdmFsdWWUjA0odXNlIGRlZmF1bHQplIwQY29t
YmluZV9wcmV2aW91c5SMCG92ZXJyaWRllIwSY29tYmluZV9zZWxlY3Rpb25zlIwDYW5klIwJY29u
ZGl0aW9ulIwAlIwbZGVmYXVsdF9jb21wYXJpc29uX29wZXJhdG9ylIwEYXV0b5SMEGRyb3BfaW1t
ZWRpYXRlbHmUiIwQaW52ZXJ0X3NlbGVjdGlvbpSJjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAAC4AAABOgAAAiEAAAJiAAAAuQAAAVkAAAIgAAACYQAAAAAAAAAAB4AA
AAC5AAABWQAAAiAAAAJhlIWUh5RSlIwJc2VsZWN0aW9ulH2UjAZNYXJrZXKUXZSMDG5vaXNlLTEw
MC1tc5Rhc4wOc2V0X2JyZWFrcG9pbnSUiXUu
</properties>
		<properties node_id="14" format="pickle">gASV5QIAAAAAAAB9lCiMDWFic29sdXRlX3RpbWWUiIwNYWx3YXlzX29uX3RvcJSJjAthbnRpYWxp
YXNlZJSIjBBhdXRvX2xpbmVfY29sb3JzlImMCWF1dG9zY2FsZZSIjBBiYWNrZ3JvdW5kX2NvbG9y
lIwHI0Y1RjVGNZSMCGNvbG9ybWFwlIwFdHVyYm+UjBBkZWNvcmF0aW9uX2NvbG9ylIwHIzAwMDAw
MJSMC2Rvd25zYW1wbGVklImMCWZvbnRfc2l6ZZRHQCQAAAAAAACMDGluaXRpYWxfZGltc5RdlChN
7gJLMk28Ak30AWWMC2xlZnRfb2Zmc2V0lEsAjApsaW5lX2NvbG9ylIwHI0NENEM0NpSMCmxpbmVf
d2lkdGiUSwGMDG1hcmtlcl9jb2xvcpSMByNGRjAwMDCUjAxtYXhfY2hhbm5lbHOUSyCMCG1ldGFk
YXRhlH2UjAxuYW5zX2FzX3plcm+UiYwObm9fY29uY2F0ZW5hdGWUiYwOb3ZlcnJpZGVfc3JhdGWU
jA0odXNlIGRlZmF1bHQplIwMcGxvdF9tYXJrZXJzlImMC3Bsb3RfbWlubWF4lImME3NhdmVkV2lk
Z2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5
dGVBcnJheZRDQgHZ0MsAAwAAAAACQgAAAMEAAATBAAADkAAAAkIAAADBAAAEwQAAA5AAAAAAAAAA
AAeAAAACQgAAAMEAAATBAAADkJSFlIeUUpSMBXNjYWxllEc/4AAAAAAAAIwOc2V0X2JyZWFrcG9p
bnSUiYwMc2hvd190b29sYmFylImMC3N0cmVhbV9uYW1llIwNKHVzZSBkZWZhdWx0KZSMCnRpbWVf
cmFuZ2WURz/pmZmZmZmajAV0aXRsZZSMBTIwMG1zlIwKemVyb19jb2xvcpSMByNBOUE5QTmUjAh6
ZXJvbWVhbpSIdS4=
</properties>
		<properties node_id="15" format="pickle">gASV5AIAAAAAAAB9lCiMDWFic29sdXRlX3RpbWWUiIwNYWx3YXlzX29uX3RvcJSJjAthbnRpYWxp
YXNlZJSIjBBhdXRvX2xpbmVfY29sb3JzlImMCWF1dG9zY2FsZZSIjBBiYWNrZ3JvdW5kX2NvbG9y
lIwHI0Y1RjVGNZSMCGNvbG9ybWFwlIwFdHVyYm+UjBBkZWNvcmF0aW9uX2NvbG9ylIwHIzAwMDAw
MJSMC2Rvd25zYW1wbGVklImMCWZvbnRfc2l6ZZRHQCQAAAAAAACMDGluaXRpYWxfZGltc5RdlChL
MksyTbwCTfQBZYwLbGVmdF9vZmZzZXSUSwCMCmxpbmVfY29sb3KUjAcjMTIyMzlFlIwKbGluZV93
aWR0aJRLAYwMbWFya2VyX2NvbG9ylIwHI0ZGMDAwMJSMDG1heF9jaGFubmVsc5RLIIwIbWV0YWRh
dGGUfZSMDG5hbnNfYXNfemVyb5SJjA5ub19jb25jYXRlbmF0ZZSJjA5vdmVycmlkZV9zcmF0ZZSM
DSh1c2UgZGVmYXVsdCmUjAxwbG90X21hcmtlcnOUiYwLcGxvdF9taW5tYXiUiYwTc2F2ZWRXaWRn
ZXRHZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0
ZUFycmF5lENCAdnQywADAAAAAAKAAAAAsAAABP8AAAN/AAACgAAAALAAAAT/AAADfwAAAAAAAAAA
B4AAAAKAAAAAsAAABP8AAAN/lIWUh5RSlIwFc2NhbGWURz/gAAAAAAAAjA5zZXRfYnJlYWtwb2lu
dJSJjAxzaG93X3Rvb2xiYXKUiYwLc3RyZWFtX25hbWWUjA0odXNlIGRlZmF1bHQplIwKdGltZV9y
YW5nZZRHP+mZmZmZmZqMBXRpdGxllIwFMTAwbXOUjAp6ZXJvX2NvbG9ylIwHI0E5QTlBOZSMCHpl
cm9tZWFulIh1Lg==
</properties>
		<properties node_id="16" format="pickle">gASVNgEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwFc3BhY2WUjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAAJeAAABnwAAA8cAAAJqAAACXwAAAb4AAAPGAAACaQAAAAAAAAAAB4AA
AAJfAAABvgAAA8YAAAJplIWUh5RSlIwJc2VsZWN0aW9ulF2UKIwCRnqUjAJDepSMAlB6lIwCT3qU
ZYwOc2V0X2JyZWFrcG9pbnSUiYwEdW5pdJSMBW5hbWVzlHUu
</properties>
		<properties node_id="17" format="pickle">gASVKQEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwEdGltZZSMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdl
b21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJy
YXmUQ0IB2dDLAAMAAAAAAwsAAAGTAAAEdAAAAl4AAAMMAAABsgAABHMAAAJdAAAAAAAAAAAHgAAA
AwwAAAGyAAAEcwAAAl2UhZSHlFKUjAlzZWxlY3Rpb26UjAcwLi4uMC45lIwOc2V0X2JyZWFrcG9p
bnSUiYwEdW5pdJSMB3NlY29uZHOUdS4=
</properties>
		<properties node_id="18" format="pickle">gASVKQEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwEdGltZZSMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdl
b21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJy
YXmUQ0IB2dDLAAMAAAAAAwsAAAGTAAAEdAAAAl4AAAMMAAABsgAABHMAAAJdAAAAAAAAAAAHgAAA
AwwAAAGyAAAEcwAAAl2UhZSHlFKUjAlzZWxlY3Rpb26UjAcwLi4uMC45lIwOc2V0X2JyZWFrcG9p
bnSUiYwEdW5pdJSMB3NlY29uZHOUdS4=
</properties>
		<properties node_id="19" format="pickle">gASVnwEAAAAAAAB9lCiME2Fzc2lnbl90YXJnZXRfdmFsdWWUjA0odXNlIGRlZmF1bHQplIwQY29t
YmluZV9wcmV2aW91c5SMCG92ZXJyaWRllIwSY29tYmluZV9zZWxlY3Rpb25zlIwDYW5klIwJY29u
ZGl0aW9ulIwAlIwbZGVmYXVsdF9jb21wYXJpc29uX29wZXJhdG9ylIwEYXV0b5SMEGRyb3BfaW1t
ZWRpYXRlbHmUiIwQaW52ZXJ0X3NlbGVjdGlvbpSJjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAAIWAAABTwAAA38AAAJ3AAACFwAAAW4AAAN+AAACdgAAAAAAAAAAB4AA
AAIXAAABbgAAA34AAAJ2lIWUh5RSlIwJc2VsZWN0aW9ulH2UjAZNYXJrZXKUXZSMDG5vaXNlLTIw
MC1tc5Rhc4wOc2V0X2JyZWFrcG9pbnSUiXUu
</properties>
		<properties node_id="20" format="pickle">gASVewEAAAAAAAB9lCiMEmFsc29fbGVnYWN5X291dHB1dJSJjA5pc19jYXRlZ29yaWNhbJSJjAlp
dl9jb2x1bW6UjAZNYXJrZXKUjAdtYXBwaW5nlF2UKIwMbm9pc2UtMTAwLW1zlIwMbm9pc2UtMjAw
LW1zlIwMbm9pc2UtMzAwLW1zlGWMDm1hcHBpbmdfZm9ybWF0lIwGY29tcGF0lIwIbWV0YWRhdGGU
fZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDUu
UXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAAC+gAAAWQAAAUpAAACPQAAAvsAAAGDAAAF
KAAAAjwAAAAAAAAAAAeAAAAC+wAAAYMAAAUoAAACPJSFlIeUUpSMDnNldF9icmVha3BvaW50lImM
EXN1cHBvcnRfd2lsZGNhcmRzlImMC3VzZV9udW1iZXJzlImMB3ZlcmJvc2WUiXUu
</properties>
		<properties node_id="21" format="pickle">gASVGAIAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiIwIY29sX2F4aXOUjAR0aW1llIwIZGVjaW1h
bHOUSwaMDWV2ZXJ5X25fdGlja3OUSwGMDWZld2VyX2J1dHRvbnOUiYwJZm9udF9zaXpllEsKjBBp
bml0aWFsX3Bvc2l0aW9ulF2UKEsUSzJN9AFNkAFljAhtZXRhZGF0YZR9lIwIcm93X2F4aXOUjAVz
cGFjZZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlR
dDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAADCwAAAUUAAAR0AAACrAAAAwwAAAFk
AAAEcwAAAqsAAAAAAAAAAAeAAAADDAAAAWQAAARzAAACq5SFlIeUUpSMDnNldF9icmVha3BvaW50
lImMD3Nob3dfYXhlc190YWJsZZSIjA9zaG93X2RhdGFfdGFibGWUiIwSc2hvd19tYXJrZXJzX3Rh
YmxllImMEHNob3dfbWF4X2NvbHVtbnOUSxSMD3Nob3dfbWF4X3ZhbHVlc5RLMowSc2hvd19zdHJl
YW1zX3RhYmxllImMC3N0cmVhbV9uYW1llIwNKHVzZSBkZWZhdWx0KZSMB3ZlcmJvc2WUiIwMd2lu
ZG93X3RpdGxllIwTSW5zcGVjdCBEYXRhIFBhY2tldJR1Lg==
</properties>
		<properties node_id="22" format="literal">{'apply_multiple_axes': False, 'apply_time_selection_to_markers': False, 'axis': 'space', 'metadata': {}, 'savedWidgetGeometry': None, 'selection': ['Fz', 'Cz', 'Pz', 'Oz'], 'set_breakpoint': False, 'unit': 'names'}</properties>
		<properties node_id="23" format="literal">{'apply_multiple_axes': False, 'apply_time_selection_to_markers': False, 'axis': 'time', 'metadata': {}, 'savedWidgetGeometry': None, 'selection': '0...0.9', 'set_breakpoint': False, 'unit': 'seconds'}</properties>
		<properties node_id="24" format="pickle">gASV5QIAAAAAAAB9lCiMDWFic29sdXRlX3RpbWWUiIwNYWx3YXlzX29uX3RvcJSJjAthbnRpYWxp
YXNlZJSIjBBhdXRvX2xpbmVfY29sb3JzlImMCWF1dG9zY2FsZZSIjBBiYWNrZ3JvdW5kX2NvbG9y
lIwHI0Y1RjVGNZSMCGNvbG9ybWFwlIwFdHVyYm+UjBBkZWNvcmF0aW9uX2NvbG9ylIwHIzAwMDAw
MJSMC2Rvd25zYW1wbGVklImMCWZvbnRfc2l6ZZRHQCQAAAAAAACMDGluaXRpYWxfZGltc5RdlChN
7gJLMk28Ak30AWWMC2xlZnRfb2Zmc2V0lEsAjApsaW5lX2NvbG9ylIwHI0NENEM0NpSMCmxpbmVf
d2lkdGiUSwGMDG1hcmtlcl9jb2xvcpSMByNGRjAwMDCUjAxtYXhfY2hhbm5lbHOUSyCMCG1ldGFk
YXRhlH2UjAxuYW5zX2FzX3plcm+UiYwObm9fY29uY2F0ZW5hdGWUiYwOb3ZlcnJpZGVfc3JhdGWU
jA0odXNlIGRlZmF1bHQplIwMcGxvdF9tYXJrZXJzlImMC3Bsb3RfbWlubWF4lImME3NhdmVkV2lk
Z2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5
dGVBcnJheZRDQgHZ0MsAAwAAAAADCwAAAIEAAAR0AAADcAAAAwwAAACgAAAEcwAAA28AAAAAAAAA
AAeAAAADDAAAAKAAAARzAAADb5SFlIeUUpSMBXNjYWxllEc/4AAAAAAAAIwOc2V0X2JyZWFrcG9p
bnSUiYwMc2hvd190b29sYmFylImMC3N0cmVhbV9uYW1llIwNKHVzZSBkZWZhdWx0KZSMCnRpbWVf
cmFuZ2WURz/pmZmZmZmajAV0aXRsZZSMBTMwMG1zlIwKemVyb19jb2xvcpSMByNBOUE5QTmUjAh6
ZXJvbWVhbpSIdS4=
</properties>
		<properties node_id="25" format="pickle">gASVnwEAAAAAAAB9lCiME2Fzc2lnbl90YXJnZXRfdmFsdWWUjA0odXNlIGRlZmF1bHQplIwQY29t
YmluZV9wcmV2aW91c5SMCG92ZXJyaWRllIwSY29tYmluZV9zZWxlY3Rpb25zlIwDYW5klIwJY29u
ZGl0aW9ulIwAlIwbZGVmYXVsdF9jb21wYXJpc29uX29wZXJhdG9ylIwEYXV0b5SMEGRyb3BfaW1t
ZWRpYXRlbHmUiIwQaW52ZXJ0X3NlbGVjdGlvbpSJjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAAMLAAABZQAABHQAAAKNAAADDAAAAYQAAARzAAACjAAAAAAAAAAAB4AA
AAMMAAABhAAABHMAAAKMlIWUh5RSlIwJc2VsZWN0aW9ulH2UjAZNYXJrZXKUXZSMDG5vaXNlLTMw
MC1tc5Rhc4wOc2V0X2JyZWFrcG9pbnSUiXUu
</properties>
	</node_properties>
	<patch>{"description": {"description": "", "license": "", "name": "pipeline", "status": "(unspecified)", "url": "", "version": "0.0.0"}, "edges": [["node1", "data", "node4", "data"], ["node1", "data", "node3", "data"], ["node4", "data", "node5", "data"], ["node5", "data", "node6", "data1"], ["node3", "data", "node6", "data2"], ["node6", "outdata", "node7", "data"], ["node10", "erp_data", "node11", "data"], ["node11", "data", "node12", "data"], ["node20", "data", "node13", "data"], ["node13", "data", "node18", "data"], ["node14", "data", "node17", "data"], ["node18", "data", "node15", "data"], ["node19", "data", "node16", "data"], ["node17", "data", "node19", "data"], ["node12", "data", "node14", "data"], ["node12", "data", "node20", "data"], ["node12", "data", "node26", "data"], ["node21", "data", "node10", "data"], ["node7", "data", "node21", "data"], ["node26", "data", "node23", "data"], ["node23", "data", "node24", "data"], ["node24", "data", "node25", "data"]], "nodes": {"node1": {"class": "ImportXDF", "module": "neuropype.nodes.file_system.ImportXDF", "params": {"cloud_account": {"customized": false, "type": "StringPort", "value": ""}, "cloud_bucket": {"customized": false, "type": "StringPort", "value": ""}, "cloud_credentials": {"customized": false, "type": "StringPort", "value": ""}, "cloud_host": {"customized": false, "type": "EnumPort", "value": "Default"}, "filename": {"customized": true, "type": "StringPort", "value": "C:/recordings/p300_2/yegor_k/3/yegor_k_p300_2_2024-01-27_19-55-04_3.xdf"}, "handle_clock_resets": {"customized": false, "type": "BoolPort", "value": true}, "handle_clock_sync": {"customized": false, "type": "BoolPort", "value": true}, "handle_jitter_removal": {"customized": false, "type": "BoolPort", "value": true}, "max_marker_len": {"customized": false, "type": "IntPort", "value": null}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "reorder_timestamps": {"customized": false, "type": "BoolPort", "value": false}, "retain_streams": {"customized": false, "type": "Port", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "use_caching": {"customized": false, "type": "BoolPort", "value": false}, "use_streamnames": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "e119a910-c526-4959-b9f1-0c4c2b56a7ab"}, "node10": {"class": "EventRelatedPotential", "module": "neuropype.nodes.neural.EventRelatedPotential", "params": {"baseline_removal_range": {"customized": true, "type": "Port", "value": "-0.3...0"}, "channel_range": {"customized": false, "type": "Port", "value": ":"}, "lowpass_cutoff": {"customized": false, "type": "ListPort", "value": []}, "max_gap_length": {"customized": false, "type": "FloatPort", "value": 0.2}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "output_measure": {"customized": true, "type": "EnumPort", "value": "trials"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "skip_baseline_removal": {"customized": false, "type": "BoolPort", "value": false}, "time_bounds": {"customized": true, "type": "Port", "value": [-0.3, 1]}}, "uuid": "4acd7f3a-82aa-46fa-a4a9-ab9c10fb5cc4"}, "node11": {"class": "GroupedMean", "module": "neuropype.nodes.statistics.GroupedMean", "params": {"allow_markers": {"customized": true, "type": "BoolPort", "value": false}, "ci_range": {"customized": false, "type": "FloatPort", "value": 0.95}, "ddof": {"customized": false, "type": "IntPort", "value": 1}, "equal_var": {"customized": false, "type": "BoolPort", "value": false}, "error_type": {"customized": false, "type": "EnumPort", "value": "none"}, "fill_cols": {"customized": false, "type": "BoolPort", "value": true}, "group_cols": {"customized": true, "type": "ListPort", "value": ["Marker"]}, "grouping_type": {"customized": false, "type": "EnumPort", "value": "levels"}, "mean_type": {"customized": false, "type": "EnumPort", "value": "mean"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": false, "type": "ListPort", "value": [0, 0]}, "use_caching": {"customized": false, "type": "BoolPort", "value": false}, "winsorize": {"customized": true, "type": "BoolPort", "value": false}}, "uuid": "1e576fdf-fb23-45e1-8af0-e95f9497e998"}, "node12": {"class": "SetStreamProperties", "module": "neuropype.nodes.utilities.SetStreamProperties", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "only_signals": {"customized": false, "type": "BoolPort", "value": false}, "properties": {"customized": true, "type": "DictPort", "value": {"has_markers": false}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}}, "uuid": "573b1fb7-118a-4849-a24a-518cf4dfa4a8"}, "node13": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "EnumPort", "value": "space"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": ["Fz", "Cz", "Pz", "Oz"]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "names"}}, "uuid": "389df5fe-e147-443f-89ee-9089669bcd2e"}, "node14": {"class": "SelectInstances", "module": "neuropype.nodes.formatting.SelectInstances", "params": {"assign_target_value": {"customized": false, "type": "FloatPort", "value": null}, "combine_previous": {"customized": false, "type": "EnumPort", "value": "override"}, "combine_selections": {"customized": false, "type": "EnumPort", "value": "and"}, "condition": {"customized": false, "type": "StringPort", "value": ""}, "default_comparison_operator": {"customized": false, "type": "EnumPort", "value": "auto"}, "drop_immediately": {"customized": false, "type": "BoolPort", "value": true}, "invert_selection": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": {"Marker": ["noise-100-ms"]}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "4e8171a2-955c-4717-832d-154540730545"}, "node15": {"class": "TimeSeriesPlot", "module": "neuropype.nodes.visualization.TimeSeriesPlot", "params": {"absolute_time": {"customized": true, "type": "BoolPort", "value": true}, "always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": false}, "autoscale": {"customized": false, "type": "BoolPort", "value": true}, "background_color": {"customized": true, "type": "StringPort", "value": "#F5F5F5"}, "colormap": {"customized": false, "type": "EnumPort", "value": "turbo"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#000000"}, "downsampled": {"customized": false, "type": "BoolPort", "value": false}, "font_size": {"customized": false, "type": "FloatPort", "value": 10.0}, "initial_dims": {"customized": true, "type": "ListPort", "value": [750, 50, 700, 500]}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "line_color": {"customized": true, "type": "StringPort", "value": "#CD4C46"}, "line_width": {"customized": true, "type": "FloatPort", "value": 1}, "marker_color": {"customized": false, "type": "Port", "value": "#FF0000"}, "max_channels": {"customized": true, "type": "IntPort", "value": 4}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nans_as_zero": {"customized": false, "type": "BoolPort", "value": false}, "no_concatenate": {"customized": false, "type": "BoolPort", "value": false}, "override_srate": {"customized": false, "type": "FloatPort", "value": null}, "plot_markers": {"customized": true, "type": "BoolPort", "value": false}, "plot_minmax": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": true, "type": "FloatPort", "value": 0.5}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "time_range": {"customized": true, "type": "FloatPort", "value": 0.8}, "title": {"customized": true, "type": "StringPort", "value": "200ms"}, "zero_color": {"customized": true, "type": "StringPort", "value": "#A9A9A9"}, "zeromean": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "b193df2d-a085-421c-bbb3-3a632aa494c3"}, "node16": {"class": "TimeSeriesPlot", "module": "neuropype.nodes.visualization.TimeSeriesPlot", "params": {"absolute_time": {"customized": true, "type": "BoolPort", "value": true}, "always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": false}, "autoscale": {"customized": false, "type": "BoolPort", "value": true}, "background_color": {"customized": true, "type": "StringPort", "value": "#F5F5F5"}, "colormap": {"customized": false, "type": "EnumPort", "value": "turbo"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#000000"}, "downsampled": {"customized": false, "type": "BoolPort", "value": false}, "font_size": {"customized": false, "type": "FloatPort", "value": 10.0}, "initial_dims": {"customized": false, "type": "ListPort", "value": [50, 50, 700, 500]}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "line_color": {"customized": true, "type": "StringPort", "value": "#12239E"}, "line_width": {"customized": true, "type": "FloatPort", "value": 1}, "marker_color": {"customized": false, "type": "Port", "value": "#FF0000"}, "max_channels": {"customized": true, "type": "IntPort", "value": 4}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nans_as_zero": {"customized": false, "type": "BoolPort", "value": false}, "no_concatenate": {"customized": false, "type": "BoolPort", "value": false}, "override_srate": {"customized": false, "type": "FloatPort", "value": null}, "plot_markers": {"customized": true, "type": "BoolPort", "value": false}, "plot_minmax": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": true, "type": "FloatPort", "value": 0.5}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "time_range": {"customized": true, "type": "FloatPort", "value": 0.8}, "title": {"customized": true, "type": "StringPort", "value": "100ms"}, "zero_color": {"customized": true, "type": "StringPort", "value": "#A9A9A9"}, "zeromean": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "c0e74cce-5cd7-4391-9303-0e4791b4c583"}, "node17": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "EnumPort", "value": "space"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": ["Fz", "Cz", "Pz", "Oz"]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "names"}}, "uuid": "b7b9762b-ef09-452e-84b4-39e95f4106cd"}, "node18": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": false, "type": "EnumPort", "value": "time"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": "0...0.9"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "seconds"}}, "uuid": "006ff5cb-e95d-4c37-ad46-9f8766acd5fe"}, "node19": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": false, "type": "EnumPort", "value": "time"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": "0...0.9"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "seconds"}}, "uuid": "825f9d5f-eb2c-45c5-a587-7f90e6497c6c"}, "node2": {"class": "ScrollPlot", "module": "neuropype.nodes.visualization.ScrollPlot", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "autoscale": {"customized": false, "type": "BoolPort", "value": true}, "background_color": {"customized": false, "type": "StringPort", "value": "#FFFFFF"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#000000"}, "downsampled": {"customized": false, "type": "BoolPort", "value": false}, "initial_dims": {"customized": false, "type": "ListPort", "value": [50, 50, 700, 500]}, "line_color": {"customized": false, "type": "StringPort", "value": "#000000"}, "line_width": {"customized": false, "type": "FloatPort", "value": 0.75}, "marker_color": {"customized": false, "type": "Port", "value": "#FF0000"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nans_as_zero": {"customized": false, "type": "BoolPort", "value": false}, "override_srate": {"customized": false, "type": "FloatPort", "value": null}, "plot_markers": {"customized": false, "type": "BoolPort", "value": true}, "scale": {"customized": true, "type": "FloatPort", "value": 0.2}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "time_range": {"customized": false, "type": "FloatPort", "value": 5.0}, "title": {"customized": false, "type": "StringPort", "value": "Time series view"}, "zero_color": {"customized": false, "type": "StringPort", "value": "#7F7F7F"}, "zeromean": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "5759401b-e8c5-417b-bef1-9404c928586f"}, "node20": {"class": "SelectInstances", "module": "neuropype.nodes.formatting.SelectInstances", "params": {"assign_target_value": {"customized": false, "type": "FloatPort", "value": null}, "combine_previous": {"customized": false, "type": "EnumPort", "value": "override"}, "combine_selections": {"customized": false, "type": "EnumPort", "value": "and"}, "condition": {"customized": false, "type": "StringPort", "value": ""}, "default_comparison_operator": {"customized": false, "type": "EnumPort", "value": "auto"}, "drop_immediately": {"customized": false, "type": "BoolPort", "value": true}, "invert_selection": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": {"Marker": ["noise-200-ms"]}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "912fb384-34af-4671-b44b-89dd85f41462"}, "node21": {"class": "AssignTargets", "module": "neuropype.nodes.machine_learning.AssignTargets", "params": {"also_legacy_output": {"customized": false, "type": "BoolPort", "value": false}, "is_categorical": {"customized": false, "type": "BoolPort", "value": false}, "iv_column": {"customized": false, "type": "StringPort", "value": "Marker"}, "mapping": {"customized": true, "type": "Port", "value": ["noise-100-ms", "noise-200-ms", "noise-300-ms"]}, "mapping_format": {"customized": false, "type": "EnumPort", "value": "compat"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "support_wildcards": {"customized": false, "type": "BoolPort", "value": false}, "use_numbers": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "824e4a10-7e34-426d-8437-be7ba3a8be8d"}, "node22": {"class": "InspectPacket", "module": "neuropype.nodes.visualization.InspectPacket", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": true}, "col_axis": {"customized": false, "type": "EnumPort", "value": "time"}, "decimals": {"customized": false, "type": "IntPort", "value": 6}, "every_n_ticks": {"customized": false, "type": "IntPort", "value": 1}, "fewer_buttons": {"customized": false, "type": "BoolPort", "value": false}, "font_size": {"customized": false, "type": "IntPort", "value": 10}, "initial_position": {"customized": false, "type": "ListPort", "value": [20, 50, 500, 400]}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "row_axis": {"customized": false, "type": "EnumPort", "value": "space"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_axes_table": {"customized": false, "type": "BoolPort", "value": true}, "show_data_table": {"customized": false, "type": "BoolPort", "value": true}, "show_markers_table": {"customized": false, "type": "BoolPort", "value": false}, "show_max_columns": {"customized": false, "type": "IntPort", "value": 20}, "show_max_values": {"customized": false, "type": "IntPort", "value": 50}, "show_streams_table": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "verbose": {"customized": false, "type": "BoolPort", "value": true}, "window_title": {"customized": false, "type": "StringPort", "value": "Inspect Data Packet"}}, "uuid": "f261ca3d-1395-4ed6-8bbf-7729767f8d79"}, "node23": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "EnumPort", "value": "space"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": ["Fz", "Cz", "Pz", "Oz"]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "names"}}, "uuid": "a09c741b-868c-4409-bb18-e774ef155238"}, "node24": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": false, "type": "EnumPort", "value": "time"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": "0...0.9"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "seconds"}}, "uuid": "0886f5c4-ea47-4655-8e9f-8373d33ddc8f"}, "node25": {"class": "TimeSeriesPlot", "module": "neuropype.nodes.visualization.TimeSeriesPlot", "params": {"absolute_time": {"customized": true, "type": "BoolPort", "value": true}, "always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": false}, "autoscale": {"customized": false, "type": "BoolPort", "value": true}, "background_color": {"customized": true, "type": "StringPort", "value": "#F5F5F5"}, "colormap": {"customized": false, "type": "EnumPort", "value": "turbo"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#000000"}, "downsampled": {"customized": false, "type": "BoolPort", "value": false}, "font_size": {"customized": false, "type": "FloatPort", "value": 10.0}, "initial_dims": {"customized": true, "type": "ListPort", "value": [750, 50, 700, 500]}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "line_color": {"customized": true, "type": "StringPort", "value": "#CD4C46"}, "line_width": {"customized": true, "type": "FloatPort", "value": 1}, "marker_color": {"customized": false, "type": "Port", "value": "#FF0000"}, "max_channels": {"customized": true, "type": "IntPort", "value": 4}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nans_as_zero": {"customized": false, "type": "BoolPort", "value": false}, "no_concatenate": {"customized": false, "type": "BoolPort", "value": false}, "override_srate": {"customized": false, "type": "FloatPort", "value": null}, "plot_markers": {"customized": true, "type": "BoolPort", "value": false}, "plot_minmax": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": true, "type": "FloatPort", "value": 0.5}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "time_range": {"customized": true, "type": "FloatPort", "value": 0.8}, "title": {"customized": true, "type": "StringPort", "value": "300ms"}, "zero_color": {"customized": true, "type": "StringPort", "value": "#A9A9A9"}, "zeromean": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "d14fded6-a86a-49c5-850f-a83bc139ef87"}, "node26": {"class": "SelectInstances", "module": "neuropype.nodes.formatting.SelectInstances", "params": {"assign_target_value": {"customized": false, "type": "FloatPort", "value": null}, "combine_previous": {"customized": false, "type": "EnumPort", "value": "override"}, "combine_selections": {"customized": false, "type": "EnumPort", "value": "and"}, "condition": {"customized": false, "type": "StringPort", "value": ""}, "default_comparison_operator": {"customized": false, "type": "EnumPort", "value": "auto"}, "drop_immediately": {"customized": false, "type": "BoolPort", "value": true}, "invert_selection": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": {"Marker": ["noise-300-ms"]}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "50c01cbf-5037-4bb3-8e55-457c4e6e451e"}, "node3": {"class": "ExtractStreams", "module": "neuropype.nodes.formatting.ExtractStreams", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection_criteria": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stream_names": {"customized": true, "type": "ListPort", "value": ["markers"]}, "support_wildcards": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "04a2a5be-fe9c-45fe-9fe4-3d729ed4e496"}, "node4": {"class": "ExtractStreams", "module": "neuropype.nodes.formatting.ExtractStreams", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection_criteria": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stream_names": {"customized": true, "type": "ListPort", "value": ["eeg"]}, "support_wildcards": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "5dfacacf-d8d5-4150-ad83-188aa8649c7c"}, "node5": {"class": "SetAxisValues", "module": "neuropype.nodes.tensor_math.SetAxisValues", "params": {"array_name": {"customized": false, "type": "StringPort", "value": null}, "axis": {"customized": true, "type": "EnumPort", "value": "space"}, "axis_label": {"customized": false, "type": "StringPort", "value": null}, "axis_occurrence": {"customized": false, "type": "IntPort", "value": 0}, "handle_existing": {"customized": false, "type": "EnumPort", "value": "replace-all"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "only_signals": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "values": {"customized": true, "type": "Port", "value": ["fp1", "fp2", "po3", "po4", "p7", "p8", "po5", "po6", "f7", "f8", "Cz", "Fz", "Pz", "Oz", "p3", "p4"]}}, "uuid": "2351137e-491a-4dc1-9415-957355a5cc09"}, "node6": {"class": "MergeStreams", "module": "neuropype.nodes.formatting.MergeStreams", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "replace_if_exists": {"customized": false, "type": "BoolPort", "value": false}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "sorting": {"customized": false, "type": "EnumPort", "value": "input"}}, "uuid": "4826f7a4-66b0-491b-ac8c-105422d1aa3f"}, "node7": {"class": "PreprocessEEG", "module": "neuropype.nodes.neural.PreprocessEEG", "params": {"bad_channel_corr_threshold": {"customized": true, "type": "FloatPort", "value": 0.7}, "bad_channel_max_broken_time": {"customized": false, "type": "FloatPort", "value": 0.4}, "bad_channel_noise_threshold": {"customized": false, "type": "FloatPort", "value": 4}, "bad_window_removal_band": {"customized": false, "type": "ListPort", "value": []}, "burst_removal_cutoff": {"customized": false, "type": "FloatPort", "value": 10.0}, "calib_seconds": {"customized": false, "type": "IntPort", "value": 0}, "channels_to_import": {"customized": false, "type": "Port", "value": "all"}, "clean_signal_range": {"customized": false, "type": "ListPort", "value": [-4, 6]}, "desired_unit": {"customized": false, "type": "EnumPort", "value": "uV"}, "export_to_h5": {"customized": false, "type": "BoolPort", "value": false}, "extra_ar_params": {"customized": false, "type": "DictPort", "value": {}}, "fix_unit": {"customized": true, "type": "BoolPort", "value": true}, "highpass_frequencies": {"customized": true, "type": "ListPort", "value": [0.1, 0.2]}, "highpass_stop_atten": {"customized": false, "type": "FloatPort", "value": 50.0}, "init_on": {"customized": false, "type": "ListPort", "value": []}, "lowpass_frequencies": {"customized": true, "type": "ListPort", "value": [15, 16]}, "lowpass_stop_atten": {"customized": true, "type": "FloatPort", "value": 80}, "max_bad_channels": {"customized": false, "type": "FloatPort", "value": 0.2}, "max_broken_time": {"customized": false, "type": "FloatPort", "value": 0.4}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "montage": {"customized": false, "type": "EnumPort", "value": "auto"}, "notch_frequency": {"customized": true, "type": "FloatPort", "value": 50.0}, "num_samples": {"customized": true, "type": "IntPort", "value": 350}, "protected_channels_during_cleaning": {"customized": false, "type": "ListPort", "value": []}, "remove_unlocalized_chans": {"customized": false, "type": "BoolPort", "value": true}, "rereferencing": {"customized": false, "type": "Port", "value": "CAR"}, "sampling_rate": {"customized": false, "type": "FloatPort", "value": null}, "scale_factor": {"customized": false, "type": "FloatPort", "value": 1.0}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "skip_interpolate": {"customized": false, "type": "BoolPort", "value": false}, "skip_preprocessing": {"customized": false, "type": "BoolPort", "value": false}, "subset_size": {"customized": true, "type": "FloatPort", "value": 0.2}, "use_caching": {"customized": true, "type": "BoolPort", "value": true}, "use_clean_window": {"customized": false, "type": "BoolPort", "value": true}, "use_notch_filter": {"customized": false, "type": "BoolPort", "value": false}, "window_len": {"customized": false, "type": "FloatPort", "value": 0.5}}, "uuid": "d3cfa5e2-9e4f-4a31-be67-2438e28e6357"}, "node8": {"class": "InsertMarkers", "module": "neuropype.nodes.markers.InsertMarkers", "params": {"anchor_marker": {"customized": true, "type": "Port", "value": "'stimulus' in Marker"}, "anchor_marker_B": {"customized": true, "type": "Port", "value": "Marker=='response-was-correct'"}, "count": {"customized": false, "type": "FloatPort", "value": 1}, "counting": {"customized": false, "type": "EnumPort", "value": "perinterval"}, "enforce_intermittent_in": {"customized": false, "type": "EnumPort", "value": "marker-span"}, "except_markers": {"customized": false, "type": "ListPort", "value": []}, "extra_limits": {"customized": false, "type": "ListPort", "value": []}, "instance_fields_from": {"customized": false, "type": "EnumPort", "value": "first"}, "intermittent_markers": {"customized": false, "type": "EnumPort", "value": "allow"}, "marker_format": {"customized": true, "type": "EnumPort", "value": "conditions"}, "max_length": {"customized": false, "type": "FloatPort", "value": null}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "min_length": {"customized": false, "type": "FloatPort", "value": null}, "mode": {"customized": true, "type": "EnumPort", "value": "marker-spanned"}, "payload": {"customized": true, "type": "Port", "value": "stim-correct"}, "placement": {"customized": false, "type": "EnumPort", "value": "equidistant"}, "random_seed": {"customized": false, "type": "IntPort", "value": 12345}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "time_limits": {"customized": true, "type": "ListPort", "value": [0, 0]}}, "uuid": "a578036d-eb84-4e49-a75b-7648f4c74aba"}, "node9": {"class": "InsertMarkers", "module": "neuropype.nodes.markers.InsertMarkers", "params": {"anchor_marker": {"customized": true, "type": "Port", "value": "'stimulus' in Marker"}, "anchor_marker_B": {"customized": true, "type": "Port", "value": "Marker=='response-was-incorrect'"}, "count": {"customized": false, "type": "FloatPort", "value": 1}, "counting": {"customized": false, "type": "EnumPort", "value": "perinterval"}, "enforce_intermittent_in": {"customized": false, "type": "EnumPort", "value": "marker-span"}, "except_markers": {"customized": false, "type": "ListPort", "value": []}, "extra_limits": {"customized": false, "type": "ListPort", "value": []}, "instance_fields_from": {"customized": false, "type": "EnumPort", "value": "first"}, "intermittent_markers": {"customized": false, "type": "EnumPort", "value": "allow"}, "marker_format": {"customized": true, "type": "EnumPort", "value": "conditions"}, "max_length": {"customized": false, "type": "FloatPort", "value": null}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "min_length": {"customized": false, "type": "FloatPort", "value": null}, "mode": {"customized": true, "type": "EnumPort", "value": "marker-spanned"}, "payload": {"customized": true, "type": "Port", "value": "stim-incorrect"}, "placement": {"customized": false, "type": "EnumPort", "value": "equidistant"}, "random_seed": {"customized": false, "type": "IntPort", "value": 12345}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "time_limits": {"customized": true, "type": "ListPort", "value": [0, 0]}}, "uuid": "d794b196-cbf3-4e8f-a49c-be674ac3da18"}}, "version": 1.1}</patch>
</scheme>
