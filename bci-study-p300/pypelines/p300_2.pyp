<?xml version='1.0' encoding='utf-8'?>
<scheme version="2.0" title="pipeline" description="">
	<nodes>
		<node id="0" name="Import XDF" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" project_name="NeuroPype" version="1.4.3" title="Import XDF" uuid="b095e220-3874-4fcb-9a2f-facf07e00209" position="(293.0, 293.0)" />
		<node id="1" name="Extract Streams" qualified_name="widgets.formatting.owextractstreams.OWExtractStreams" project_name="NeuroPype" version="2.2.1" title="Extract Streams" uuid="e45a6480-3058-4399-bd81-78a0575604b6" position="(446.0, 346.0)" />
		<node id="2" name="Extract Streams" qualified_name="widgets.formatting.owextractstreams.OWExtractStreams" project_name="NeuroPype" version="2.2.1" title="Extract Streams" uuid="2ed73f3f-9259-46b5-ad1b-9c5b3d04340b" position="(406.0, 203.0)" />
		<node id="3" name="Set Axis Values" qualified_name="widgets.tensor_math.owsetaxisvalues.OWSetAxisValues" project_name="NeuroPype" version="0.2.0" title="Set Axis Values" uuid="e014e3b3-4072-481b-a548-6c8771c98000" position="(528.0, 203.0)" />
		<node id="4" name="Merge Streams" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" project_name="NeuroPype" version="1.0.0" title="Merge Streams" uuid="ea8adcb0-67a4-45ef-bef4-d132507100cc" position="(626.0, 267.0)" />
		<node id="5" name="Preprocess EEG (Meta)" qualified_name="widgets.neural.owpreprocesseeg.OWPreprocessEEG" project_name="NeuroPype" version="1.2.2" title="PreprocessEEG (Meta)" uuid="03980fd6-f356-4134-859d-679754e3f91a" position="(814.4740796393687, 272.58677685950414)" />
		<node id="6" name="Event Related Potential (Meta)" qualified_name="widgets.neural.oweventrelatedpotential.OWEventRelatedPotential" project_name="NeuroPype" version="1.0.2" title="Event Related Potential (Meta)" uuid="133e5ada-8c29-4c73-8bc3-8836e0b092a1" position="(1043.3801652892566, 305.52066115702485)" />
		<node id="7" name="Grouped Mean" qualified_name="widgets.statistics.owgroupedmean.OWGroupedMean" project_name="NeuroPype" version="1.1.0" title="Grouped Mean" uuid="4fbd6aaf-b263-4b16-9097-beee2e28291a" position="(1214.3966942148759, 314.87603305785126)" />
		<node id="8" name="Set Stream Properties" qualified_name="widgets.utilities.owsetstreamproperties.OWSetStreamProperties" project_name="NeuroPype" version="1.3.2" title="Set Stream Properties" uuid="e07efee6-dc12-4cf5-ad5f-8d027fd2efbe" position="(1342.97520661157, 325.6198347107439)" />
		<node id="9" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Filter Channels (midline)" uuid="34d90380-8911-43a8-91ae-ff0f5114ee7f" position="(1553.0661157024792, 368.42148760330576)" />
		<node id="10" name="Select Instances" qualified_name="widgets.formatting.owselectinstances.OWSelectInstances" project_name="NeuroPype" version="1.1.1" title="Select correct" uuid="3beeb5d2-5f39-4fce-9c7e-47b584cfeed8" position="(1452.0661157024792, 269.42148760330576)" />
		<node id="11" name="Time Series Plot" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" project_name="NeuroPype" version="1.2.0" title="Time Series Plot" uuid="ac592d55-6bc9-420c-b1fd-a76de9c462ff" position="(1750.157024793388, 368.42148760330576)" />
		<node id="12" name="Time Series Plot" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" project_name="NeuroPype" version="1.2.0" title="Time Series Plot" uuid="8e023b9a-803a-49fe-8e92-1140a2c9ae4c" position="(1751.2396694214879, 269.42148760330576)" />
		<node id="13" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Filter Channels (midline)" uuid="c0effdcb-9c52-4198-a9b4-82acbe2baf80" position="(1552.0661157024792, 269.42148760330576)" />
		<node id="14" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Select Range" uuid="6e473daf-a88d-43a0-85c9-f6d43c72c2c0" position="(1650.0661157024792, 370.42148760330576)" />
		<node id="15" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Select Range" uuid="a0de296c-ca23-4ee5-a183-55b9a07bd64c" position="(1653.8842975206612, 269.4214876033057)" />
		<node id="16" name="Select Instances" qualified_name="widgets.formatting.owselectinstances.OWSelectInstances" project_name="NeuroPype" version="1.1.1" title="Select incorrect" uuid="3c614d05-556c-4eab-aa08-dc380d67266c" position="(1452.0661157024792, 369.42148760330576)" />
		<node id="17" name="Assign Target Values" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" project_name="NeuroPype" version="1.0.1" title="Assign Target Values" uuid="40f9c46f-c326-4949-a21c-c6913dcd652a" position="(941.4049586776857, 287.47933884297515)" />
		<node id="18" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Filter Channels (midline)" uuid="e90b453f-831d-42c1-a988-0f5fe1371fc1" position="(1553.9752066115705, 463.87603305785126)" />
		<node id="19" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Select Range" uuid="1374533c-01ca-4e92-a16e-832b5b8940e8" position="(1650.9752066115705, 465.87603305785126)" />
		<node id="20" name="Time Series Plot" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" project_name="NeuroPype" version="1.2.0" title="Time Series Plot" uuid="29b37aa8-a72d-40f6-945b-274495dc1bb6" position="(1751.066115702479, 463.87603305785126)" />
		<node id="21" name="Select Instances" qualified_name="widgets.formatting.owselectinstances.OWSelectInstances" project_name="NeuroPype" version="1.1.1" title="Select incorrect" uuid="48471158-8e0a-4862-90dc-d54d98b25db0" position="(1452.9752066115705, 464.87603305785126)" />
	</nodes>
	<links>
		<link id="0" source_node_id="0" sink_node_id="2" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="1" source_node_id="0" sink_node_id="1" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="2" source_node_id="2" sink_node_id="3" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="3" source_node_id="3" sink_node_id="4" source_channel="Data" sink_channel="Data1" enabled="true" />
		<link id="4" source_node_id="1" sink_node_id="4" source_channel="Data" sink_channel="Data2" enabled="true" />
		<link id="5" source_node_id="4" sink_node_id="5" source_channel="Outdata" sink_channel="Data" enabled="true" />
		<link id="6" source_node_id="6" sink_node_id="7" source_channel="Erp Data" sink_channel="Data" enabled="true" />
		<link id="7" source_node_id="7" sink_node_id="8" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="8" source_node_id="16" sink_node_id="9" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="9" source_node_id="9" sink_node_id="14" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="10" source_node_id="10" sink_node_id="13" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="11" source_node_id="14" sink_node_id="11" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="12" source_node_id="15" sink_node_id="12" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="13" source_node_id="13" sink_node_id="15" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="14" source_node_id="8" sink_node_id="10" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="15" source_node_id="8" sink_node_id="16" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="16" source_node_id="17" sink_node_id="6" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="17" source_node_id="5" sink_node_id="17" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="18" source_node_id="21" sink_node_id="18" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="19" source_node_id="18" sink_node_id="19" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="20" source_node_id="19" sink_node_id="20" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="21" source_node_id="8" sink_node_id="21" source_channel="Data" sink_channel="Data" enabled="true" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties node_id="0" format="pickle">gASV1AEAAAAAAAB9lCiMDWNsb3VkX2FjY291bnSUjACUjAxjbG91ZF9idWNrZXSUaAKMEWNsb3Vk
X2NyZWRlbnRpYWxzlGgCjApjbG91ZF9ob3N0lIwHRGVmYXVsdJSMCGZpbGVuYW1llGgCjBNoYW5k
bGVfY2xvY2tfcmVzZXRzlIiMEWhhbmRsZV9jbG9ja19zeW5jlIiMFWhhbmRsZV9qaXR0ZXJfcmVt
b3ZhbJSIjA5tYXhfbWFya2VyX2xlbpSMDSh1c2UgZGVmYXVsdCmUjAhtZXRhZGF0YZR9lIwScmVv
cmRlcl90aW1lc3RhbXBzlImMDnJldGFpbl9zdHJlYW1zlGgMjBNzYXZlZFdpZGdldEdlb21ldHJ5
lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB
2dDLAAMAAAAAAwwAAAGZAAAEcwAAAncAAAMMAAABmQAABHMAAAJ3AAAAAAAAAAAHgAAAAwwAAAGZ
AAAEcwAAAneUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAt1c2VfY2FjaGluZ5SJjA91c2Vfc3Ry
ZWFtbmFtZXOUiYwHdmVyYm9zZZSJdS4=
</properties>
		<properties node_id="1" format="pickle">gASVDQEAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwO
X3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAA
AwsAAAGVAAAEdAAAAl0AAAMMAAABtAAABHMAAAJcAAAAAAAAAAAHgAAAAwwAAAG0AAAEcwAAAlyU
hZSHlFKUjBJzZWxlY3Rpb25fY3JpdGVyaWGUfZSMDnNldF9icmVha3BvaW50lImMDHN0cmVhbV9u
YW1lc5RdlIwHbWFya2Vyc5RhjBFzdXBwb3J0X3dpbGRjYXJkc5SJjAd2ZXJib3NllIl1Lg==
</properties>
		<properties node_id="2" format="pickle">gASVCQEAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwO
X3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAA
AwsAAAGVAAAEdAAAAl0AAAMMAAABtAAABHMAAAJcAAAAAAAAAAAHgAAAAwwAAAG0AAAEcwAAAlyU
hZSHlFKUjBJzZWxlY3Rpb25fY3JpdGVyaWGUfZSMDnNldF9icmVha3BvaW50lImMDHN0cmVhbV9u
YW1lc5RdlIwDZWVnlGGMEXN1cHBvcnRfd2lsZGNhcmRzlImMB3ZlcmJvc2WUiXUu
</properties>
		<properties node_id="3" format="pickle">gASVqgEAAAAAAAB9lCiMCmFycmF5X25hbWWUjA0odXNlIGRlZmF1bHQplIwEYXhpc5SMBXNwYWNl
lIwKYXhpc19sYWJlbJSMDSh1c2UgZGVmYXVsdCmUjA9heGlzX29jY3VycmVuY2WUSwCMD2hhbmRs
ZV9leGlzdGluZ5SMC3JlcGxhY2UtYWxslIwIbWV0YWRhdGGUfZSMDG9ubHlfc2lnbmFsc5SIjBNz
YXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29y
ZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAABA0AAAFJAAAFdgAAAhcAAAQOAAABaAAABXUAAAIW
AAAAAAAAAAAHgAAABA4AAAFoAAAFdQAAAhaUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAZ2YWx1
ZXOUXZQojANmcDGUjANmcDKUjANwbzOUjANwbzSUjAJwN5SMAnA4lIwDcG81lIwDcG82lIwCZjeU
jAJmOJSMAkN6lIwCRnqUjAJQepSMAk96lIwCcDOUjAJwNJRldS4=
</properties>
		<properties node_id="4" format="pickle">gASV4QAAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjBFyZXBsYWNlX2lmX2V4aXN0c5SJjBNzYXZlZFdp
ZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFC
eXRlQXJyYXmUQ0IB2dDLAAMAAAAAAwsAAAGrAAAEdAAAAkYAAAMMAAABygAABHMAAAJFAAAAAAAA
AAAHgAAAAwwAAAHKAAAEcwAAAkWUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAdzb3J0aW5nlIwF
aW5wdXSUdS4=
</properties>
		<properties node_id="5" format="pickle">gASVFAQAAAAAAAB9lCiMGmJhZF9jaGFubmVsX2NvcnJfdGhyZXNob2xklEc/5mZmZmZmZowbYmFk
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
		<properties node_id="6" format="pickle">gASVbwEAAAAAAAB9lCiMFmJhc2VsaW5lX3JlbW92YWxfcmFuZ2WUjAgtMC4zLi4uMJSMDWNoYW5u
ZWxfcmFuZ2WUjAE6lIwObG93cGFzc19jdXRvZmaUXZSMDm1heF9nYXBfbGVuZ3RolEc/yZmZmZmZ
mowIbWV0YWRhdGGUfZSMDm91dHB1dF9tZWFzdXJllIwGdHJpYWxzlIwTc2F2ZWRXaWRnZXRHZW9t
ZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFycmF5
lENCAdnQywADAAAAAAL9AAABSQAABGQAAAJcAAAC/QAAAUkAAARkAAACXAAAAAAAAAAAB4AAAAL9
AAABSQAABGQAAAJclIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwVc2tpcF9iYXNlbGluZV9yZW1v
dmFslImMC3RpbWVfYm91bmRzlF2UKEe/0zMzMzMzM0sBZXUu
</properties>
		<properties node_id="7" format="pickle">gASVkQEAAAAAAAB9lCiMDWFsbG93X21hcmtlcnOUiYwIY2lfcmFuZ2WURz/uZmZmZmZmjARkZG9m
lEsBjAllcXVhbF92YXKUiYwKZXJyb3JfdHlwZZSMBG5vbmWUjAlmaWxsX2NvbHOUiIwKZ3JvdXBf
Y29sc5RdlIwGTWFya2VylGGMDWdyb3VwaW5nX3R5cGWUjAZsZXZlbHOUjAltZWFuX3R5cGWUjARt
ZWFulIwIbWV0YWRhdGGUfZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVf
dHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAADCwAAAX0AAAR0
AAACdQAAAwwAAAGcAAAEcwAAAnQAAAAAAAAAAAeAAAADDAAAAZwAAARzAAACdJSFlIeUUpSMDnNl
dF9icmVha3BvaW50lImMD3RyaW1fcHJvcG9ydGlvbpRdlChLAEsAZYwLdXNlX2NhY2hpbmeUiYwJ
d2luc29yaXpllIl1Lg==
</properties>
		<properties node_id="8" format="pickle">gASVBwEAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjAxvbmx5X3NpZ25hbHOUiYwKcHJvcGVydGllc5R9
lIwLaGFzX21hcmtlcnOUiXOME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVf
dHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAADCwAAAaoAAAR0
AAACSAAAAwwAAAHJAAAEcwAAAkcAAAAAAAAAAAeAAAADDAAAAckAAARzAAACR5SFlIeUUpSMDnNl
dF9icmVha3BvaW50lImMC3N0cmVhbV9uYW1llIwNKHVzZSBkZWZhdWx0KZR1Lg==
</properties>
		<properties node_id="9" format="pickle">gASVNgEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwFc3BhY2WUjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAAMLAAABkwAABHQAAAJeAAADDAAAAbIAAARzAAACXQAAAAAAAAAAB4AA
AAMMAAABsgAABHMAAAJdlIWUh5RSlIwJc2VsZWN0aW9ulF2UKIwCRnqUjAJDepSMAlB6lIwCT3qU
ZYwOc2V0X2JyZWFrcG9pbnSUiYwEdW5pdJSMBW5hbWVzlHUu
</properties>
		<properties node_id="10" format="pickle">gASVnwEAAAAAAAB9lCiME2Fzc2lnbl90YXJnZXRfdmFsdWWUjA0odXNlIGRlZmF1bHQplIwQY29t
YmluZV9wcmV2aW91c5SMCG92ZXJyaWRllIwSY29tYmluZV9zZWxlY3Rpb25zlIwDYW5klIwJY29u
ZGl0aW9ulIwAlIwbZGVmYXVsdF9jb21wYXJpc29uX29wZXJhdG9ylIwEYXV0b5SMEGRyb3BfaW1t
ZWRpYXRlbHmUiIwQaW52ZXJ0X3NlbGVjdGlvbpSJjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAAC4AAABOgAAAiEAAAJiAAAAuQAAAVkAAAIgAAACYQAAAAAAAAAAB4AA
AAC5AAABWQAAAiAAAAJhlIWUh5RSlIwJc2VsZWN0aW9ulH2UjAZNYXJrZXKUXZSMDG5vaXNlLTEw
MC1tc5Rhc4wOc2V0X2JyZWFrcG9pbnSUiXUu
</properties>
		<properties node_id="11" format="pickle">gASV5QIAAAAAAAB9lCiMDWFic29sdXRlX3RpbWWUiIwNYWx3YXlzX29uX3RvcJSJjAthbnRpYWxp
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
		<properties node_id="12" format="pickle">gASV5AIAAAAAAAB9lCiMDWFic29sdXRlX3RpbWWUiIwNYWx3YXlzX29uX3RvcJSJjAthbnRpYWxp
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
		<properties node_id="13" format="pickle">gASVNgEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwFc3BhY2WUjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAAJeAAABnwAAA8cAAAJqAAACXwAAAb4AAAPGAAACaQAAAAAAAAAAB4AA
AAJfAAABvgAAA8YAAAJplIWUh5RSlIwJc2VsZWN0aW9ulF2UKIwCRnqUjAJDepSMAlB6lIwCT3qU
ZYwOc2V0X2JyZWFrcG9pbnSUiYwEdW5pdJSMBW5hbWVzlHUu
</properties>
		<properties node_id="14" format="pickle">gASVKQEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwEdGltZZSMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdl
b21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJy
YXmUQ0IB2dDLAAMAAAAAAwsAAAGTAAAEdAAAAl4AAAMMAAABsgAABHMAAAJdAAAAAAAAAAAHgAAA
AwwAAAGyAAAEcwAAAl2UhZSHlFKUjAlzZWxlY3Rpb26UjAcwLi4uMC45lIwOc2V0X2JyZWFrcG9p
bnSUiYwEdW5pdJSMB3NlY29uZHOUdS4=
</properties>
		<properties node_id="15" format="pickle">gASVKQEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwEdGltZZSMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdl
b21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJy
YXmUQ0IB2dDLAAMAAAAAAwsAAAGTAAAEdAAAAl4AAAMMAAABsgAABHMAAAJdAAAAAAAAAAAHgAAA
AwwAAAGyAAAEcwAAAl2UhZSHlFKUjAlzZWxlY3Rpb26UjAcwLi4uMC45lIwOc2V0X2JyZWFrcG9p
bnSUiYwEdW5pdJSMB3NlY29uZHOUdS4=
</properties>
		<properties node_id="16" format="pickle">gASVnwEAAAAAAAB9lCiME2Fzc2lnbl90YXJnZXRfdmFsdWWUjA0odXNlIGRlZmF1bHQplIwQY29t
YmluZV9wcmV2aW91c5SMCG92ZXJyaWRllIwSY29tYmluZV9zZWxlY3Rpb25zlIwDYW5klIwJY29u
ZGl0aW9ulIwAlIwbZGVmYXVsdF9jb21wYXJpc29uX29wZXJhdG9ylIwEYXV0b5SMEGRyb3BfaW1t
ZWRpYXRlbHmUiIwQaW52ZXJ0X3NlbGVjdGlvbpSJjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAAIWAAABTwAAA38AAAJ3AAACFwAAAW4AAAN+AAACdgAAAAAAAAAAB4AA
AAIXAAABbgAAA34AAAJ2lIWUh5RSlIwJc2VsZWN0aW9ulH2UjAZNYXJrZXKUXZSMDG5vaXNlLTIw
MC1tc5Rhc4wOc2V0X2JyZWFrcG9pbnSUiXUu
</properties>
		<properties node_id="17" format="pickle">gASVewEAAAAAAAB9lCiMEmFsc29fbGVnYWN5X291dHB1dJSJjA5pc19jYXRlZ29yaWNhbJSJjAlp
dl9jb2x1bW6UjAZNYXJrZXKUjAdtYXBwaW5nlF2UKIwMbm9pc2UtMTAwLW1zlIwMbm9pc2UtMjAw
LW1zlIwMbm9pc2UtMzAwLW1zlGWMDm1hcHBpbmdfZm9ybWF0lIwGY29tcGF0lIwIbWV0YWRhdGGU
fZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDUu
UXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAADHgAAAVAAAAVNAAACKQAAAx8AAAFvAAAF
TAAAAigAAAAAAAAAAAeAAAADHwAAAW8AAAVMAAACKJSFlIeUUpSMDnNldF9icmVha3BvaW50lImM
EXN1cHBvcnRfd2lsZGNhcmRzlImMC3VzZV9udW1iZXJzlImMB3ZlcmJvc2WUiXUu
</properties>
		<properties node_id="18" format="literal">{'apply_multiple_axes': False, 'apply_time_selection_to_markers': False, 'axis': 'space', 'metadata': {}, 'savedWidgetGeometry': None, 'selection': ['Fz', 'Cz', 'Pz', 'Oz'], 'set_breakpoint': False, 'unit': 'names'}</properties>
		<properties node_id="19" format="literal">{'apply_multiple_axes': False, 'apply_time_selection_to_markers': False, 'axis': 'time', 'metadata': {}, 'savedWidgetGeometry': None, 'selection': '0...0.9', 'set_breakpoint': False, 'unit': 'seconds'}</properties>
		<properties node_id="20" format="pickle">gASV5QIAAAAAAAB9lCiMDWFic29sdXRlX3RpbWWUiIwNYWx3YXlzX29uX3RvcJSJjAthbnRpYWxp
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
		<properties node_id="21" format="pickle">gASVnwEAAAAAAAB9lCiME2Fzc2lnbl90YXJnZXRfdmFsdWWUjA0odXNlIGRlZmF1bHQplIwQY29t
YmluZV9wcmV2aW91c5SMCG92ZXJyaWRllIwSY29tYmluZV9zZWxlY3Rpb25zlIwDYW5klIwJY29u
ZGl0aW9ulIwAlIwbZGVmYXVsdF9jb21wYXJpc29uX29wZXJhdG9ylIwEYXV0b5SMEGRyb3BfaW1t
ZWRpYXRlbHmUiIwQaW52ZXJ0X3NlbGVjdGlvbpSJjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAAMLAAABZQAABHQAAAKNAAADDAAAAYQAAARzAAACjAAAAAAAAAAAB4AA
AAMMAAABhAAABHMAAAKMlIWUh5RSlIwJc2VsZWN0aW9ulH2UjAZNYXJrZXKUXZSMDG5vaXNlLTMw
MC1tc5Rhc4wOc2V0X2JyZWFrcG9pbnSUiXUu
</properties>
	</node_properties>
	<patch>{"description": {"description": "", "license": "", "name": "pipeline", "status": "(unspecified)", "url": "", "version": "0.0.0"}, "edges": [["node1", "data", "node3", "data"], ["node1", "data", "node2", "data"], ["node3", "data", "node4", "data"], ["node4", "data", "node5", "data1"], ["node2", "data", "node5", "data2"], ["node5", "outdata", "node6", "data"], ["node7", "erp_data", "node8", "data"], ["node8", "data", "node9", "data"], ["node17", "data", "node10", "data"], ["node10", "data", "node15", "data"], ["node11", "data", "node14", "data"], ["node15", "data", "node12", "data"], ["node16", "data", "node13", "data"], ["node14", "data", "node16", "data"], ["node9", "data", "node11", "data"], ["node9", "data", "node17", "data"], ["node9", "data", "node22", "data"], ["node18", "data", "node7", "data"], ["node6", "data", "node18", "data"], ["node22", "data", "node19", "data"], ["node19", "data", "node20", "data"], ["node20", "data", "node21", "data"]], "nodes": {"node1": {"class": "ImportXDF", "module": "neuropype.nodes.file_system.ImportXDF", "params": {"cloud_account": {"customized": false, "type": "StringPort", "value": ""}, "cloud_bucket": {"customized": false, "type": "StringPort", "value": ""}, "cloud_credentials": {"customized": false, "type": "StringPort", "value": ""}, "cloud_host": {"customized": false, "type": "EnumPort", "value": "Default"}, "filename": {"customized": false, "type": "StringPort", "value": ""}, "handle_clock_resets": {"customized": false, "type": "BoolPort", "value": true}, "handle_clock_sync": {"customized": false, "type": "BoolPort", "value": true}, "handle_jitter_removal": {"customized": false, "type": "BoolPort", "value": true}, "max_marker_len": {"customized": false, "type": "IntPort", "value": null}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "reorder_timestamps": {"customized": false, "type": "BoolPort", "value": false}, "retain_streams": {"customized": false, "type": "Port", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "use_caching": {"customized": false, "type": "BoolPort", "value": false}, "use_streamnames": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "b095e220-3874-4fcb-9a2f-facf07e00209"}, "node10": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "EnumPort", "value": "space"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": ["Fz", "Cz", "Pz", "Oz"]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "names"}}, "uuid": "34d90380-8911-43a8-91ae-ff0f5114ee7f"}, "node11": {"class": "SelectInstances", "module": "neuropype.nodes.formatting.SelectInstances", "params": {"assign_target_value": {"customized": false, "type": "FloatPort", "value": null}, "combine_previous": {"customized": false, "type": "EnumPort", "value": "override"}, "combine_selections": {"customized": false, "type": "EnumPort", "value": "and"}, "condition": {"customized": false, "type": "StringPort", "value": ""}, "default_comparison_operator": {"customized": false, "type": "EnumPort", "value": "auto"}, "drop_immediately": {"customized": false, "type": "BoolPort", "value": true}, "invert_selection": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": {"Marker": ["noise-100-ms"]}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "3beeb5d2-5f39-4fce-9c7e-47b584cfeed8"}, "node12": {"class": "TimeSeriesPlot", "module": "neuropype.nodes.visualization.TimeSeriesPlot", "params": {"absolute_time": {"customized": true, "type": "BoolPort", "value": true}, "always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": false}, "autoscale": {"customized": false, "type": "BoolPort", "value": true}, "background_color": {"customized": true, "type": "StringPort", "value": "#F5F5F5"}, "colormap": {"customized": false, "type": "EnumPort", "value": "turbo"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#000000"}, "downsampled": {"customized": false, "type": "BoolPort", "value": false}, "font_size": {"customized": false, "type": "FloatPort", "value": 10.0}, "initial_dims": {"customized": true, "type": "ListPort", "value": [750, 50, 700, 500]}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "line_color": {"customized": true, "type": "StringPort", "value": "#CD4C46"}, "line_width": {"customized": true, "type": "FloatPort", "value": 1}, "marker_color": {"customized": false, "type": "Port", "value": "#FF0000"}, "max_channels": {"customized": false, "type": "IntPort", "value": 32}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nans_as_zero": {"customized": false, "type": "BoolPort", "value": false}, "no_concatenate": {"customized": false, "type": "BoolPort", "value": false}, "override_srate": {"customized": false, "type": "FloatPort", "value": null}, "plot_markers": {"customized": true, "type": "BoolPort", "value": false}, "plot_minmax": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": true, "type": "FloatPort", "value": 0.5}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "time_range": {"customized": true, "type": "FloatPort", "value": 0.8}, "title": {"customized": true, "type": "StringPort", "value": "200ms"}, "zero_color": {"customized": true, "type": "StringPort", "value": "#A9A9A9"}, "zeromean": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "ac592d55-6bc9-420c-b1fd-a76de9c462ff"}, "node13": {"class": "TimeSeriesPlot", "module": "neuropype.nodes.visualization.TimeSeriesPlot", "params": {"absolute_time": {"customized": true, "type": "BoolPort", "value": true}, "always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": false}, "autoscale": {"customized": false, "type": "BoolPort", "value": true}, "background_color": {"customized": true, "type": "StringPort", "value": "#F5F5F5"}, "colormap": {"customized": false, "type": "EnumPort", "value": "turbo"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#000000"}, "downsampled": {"customized": false, "type": "BoolPort", "value": false}, "font_size": {"customized": false, "type": "FloatPort", "value": 10.0}, "initial_dims": {"customized": false, "type": "ListPort", "value": [50, 50, 700, 500]}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "line_color": {"customized": true, "type": "StringPort", "value": "#12239E"}, "line_width": {"customized": true, "type": "FloatPort", "value": 1}, "marker_color": {"customized": false, "type": "Port", "value": "#FF0000"}, "max_channels": {"customized": false, "type": "IntPort", "value": 32}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nans_as_zero": {"customized": false, "type": "BoolPort", "value": false}, "no_concatenate": {"customized": false, "type": "BoolPort", "value": false}, "override_srate": {"customized": false, "type": "FloatPort", "value": null}, "plot_markers": {"customized": true, "type": "BoolPort", "value": false}, "plot_minmax": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": true, "type": "FloatPort", "value": 0.5}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "time_range": {"customized": true, "type": "FloatPort", "value": 0.8}, "title": {"customized": true, "type": "StringPort", "value": "100ms"}, "zero_color": {"customized": true, "type": "StringPort", "value": "#A9A9A9"}, "zeromean": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "8e023b9a-803a-49fe-8e92-1140a2c9ae4c"}, "node14": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "EnumPort", "value": "space"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": ["Fz", "Cz", "Pz", "Oz"]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "names"}}, "uuid": "c0effdcb-9c52-4198-a9b4-82acbe2baf80"}, "node15": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": false, "type": "EnumPort", "value": "time"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": "0...0.9"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "seconds"}}, "uuid": "6e473daf-a88d-43a0-85c9-f6d43c72c2c0"}, "node16": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": false, "type": "EnumPort", "value": "time"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": "0...0.9"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "seconds"}}, "uuid": "a0de296c-ca23-4ee5-a183-55b9a07bd64c"}, "node17": {"class": "SelectInstances", "module": "neuropype.nodes.formatting.SelectInstances", "params": {"assign_target_value": {"customized": false, "type": "FloatPort", "value": null}, "combine_previous": {"customized": false, "type": "EnumPort", "value": "override"}, "combine_selections": {"customized": false, "type": "EnumPort", "value": "and"}, "condition": {"customized": false, "type": "StringPort", "value": ""}, "default_comparison_operator": {"customized": false, "type": "EnumPort", "value": "auto"}, "drop_immediately": {"customized": false, "type": "BoolPort", "value": true}, "invert_selection": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": {"Marker": ["noise-200-ms"]}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "3c614d05-556c-4eab-aa08-dc380d67266c"}, "node18": {"class": "AssignTargets", "module": "neuropype.nodes.machine_learning.AssignTargets", "params": {"also_legacy_output": {"customized": false, "type": "BoolPort", "value": false}, "is_categorical": {"customized": false, "type": "BoolPort", "value": false}, "iv_column": {"customized": false, "type": "StringPort", "value": "Marker"}, "mapping": {"customized": true, "type": "Port", "value": ["noise-100-ms", "noise-200-ms", "noise-300-ms"]}, "mapping_format": {"customized": false, "type": "EnumPort", "value": "compat"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "support_wildcards": {"customized": false, "type": "BoolPort", "value": false}, "use_numbers": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "40f9c46f-c326-4949-a21c-c6913dcd652a"}, "node19": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "EnumPort", "value": "space"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": ["Fz", "Cz", "Pz", "Oz"]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "names"}}, "uuid": "e90b453f-831d-42c1-a988-0f5fe1371fc1"}, "node2": {"class": "ExtractStreams", "module": "neuropype.nodes.formatting.ExtractStreams", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection_criteria": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stream_names": {"customized": true, "type": "ListPort", "value": ["markers"]}, "support_wildcards": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "e45a6480-3058-4399-bd81-78a0575604b6"}, "node20": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": false, "type": "EnumPort", "value": "time"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": "0...0.9"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "seconds"}}, "uuid": "1374533c-01ca-4e92-a16e-832b5b8940e8"}, "node21": {"class": "TimeSeriesPlot", "module": "neuropype.nodes.visualization.TimeSeriesPlot", "params": {"absolute_time": {"customized": true, "type": "BoolPort", "value": true}, "always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": false}, "autoscale": {"customized": false, "type": "BoolPort", "value": true}, "background_color": {"customized": true, "type": "StringPort", "value": "#F5F5F5"}, "colormap": {"customized": false, "type": "EnumPort", "value": "turbo"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#000000"}, "downsampled": {"customized": false, "type": "BoolPort", "value": false}, "font_size": {"customized": false, "type": "FloatPort", "value": 10.0}, "initial_dims": {"customized": true, "type": "ListPort", "value": [750, 50, 700, 500]}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "line_color": {"customized": true, "type": "StringPort", "value": "#CD4C46"}, "line_width": {"customized": true, "type": "FloatPort", "value": 1}, "marker_color": {"customized": false, "type": "Port", "value": "#FF0000"}, "max_channels": {"customized": false, "type": "IntPort", "value": 32}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nans_as_zero": {"customized": false, "type": "BoolPort", "value": false}, "no_concatenate": {"customized": false, "type": "BoolPort", "value": false}, "override_srate": {"customized": false, "type": "FloatPort", "value": null}, "plot_markers": {"customized": true, "type": "BoolPort", "value": false}, "plot_minmax": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": true, "type": "FloatPort", "value": 0.5}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "time_range": {"customized": true, "type": "FloatPort", "value": 0.8}, "title": {"customized": true, "type": "StringPort", "value": "300ms"}, "zero_color": {"customized": true, "type": "StringPort", "value": "#A9A9A9"}, "zeromean": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "29b37aa8-a72d-40f6-945b-274495dc1bb6"}, "node22": {"class": "SelectInstances", "module": "neuropype.nodes.formatting.SelectInstances", "params": {"assign_target_value": {"customized": false, "type": "FloatPort", "value": null}, "combine_previous": {"customized": false, "type": "EnumPort", "value": "override"}, "combine_selections": {"customized": false, "type": "EnumPort", "value": "and"}, "condition": {"customized": false, "type": "StringPort", "value": ""}, "default_comparison_operator": {"customized": false, "type": "EnumPort", "value": "auto"}, "drop_immediately": {"customized": false, "type": "BoolPort", "value": true}, "invert_selection": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": {"Marker": ["noise-300-ms"]}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "48471158-8e0a-4862-90dc-d54d98b25db0"}, "node3": {"class": "ExtractStreams", "module": "neuropype.nodes.formatting.ExtractStreams", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection_criteria": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stream_names": {"customized": true, "type": "ListPort", "value": ["eeg"]}, "support_wildcards": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "2ed73f3f-9259-46b5-ad1b-9c5b3d04340b"}, "node4": {"class": "SetAxisValues", "module": "neuropype.nodes.tensor_math.SetAxisValues", "params": {"array_name": {"customized": false, "type": "StringPort", "value": null}, "axis": {"customized": true, "type": "EnumPort", "value": "space"}, "axis_label": {"customized": false, "type": "StringPort", "value": null}, "axis_occurrence": {"customized": false, "type": "IntPort", "value": 0}, "handle_existing": {"customized": false, "type": "EnumPort", "value": "replace-all"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "only_signals": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "values": {"customized": true, "type": "Port", "value": ["fp1", "fp2", "po3", "po4", "p7", "p8", "po5", "po6", "f7", "f8", "Cz", "Fz", "Pz", "Oz", "p3", "p4"]}}, "uuid": "e014e3b3-4072-481b-a548-6c8771c98000"}, "node5": {"class": "MergeStreams", "module": "neuropype.nodes.formatting.MergeStreams", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "replace_if_exists": {"customized": false, "type": "BoolPort", "value": false}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "sorting": {"customized": false, "type": "EnumPort", "value": "input"}}, "uuid": "ea8adcb0-67a4-45ef-bef4-d132507100cc"}, "node6": {"class": "PreprocessEEG", "module": "neuropype.nodes.neural.PreprocessEEG", "params": {"bad_channel_corr_threshold": {"customized": true, "type": "FloatPort", "value": 0.7}, "bad_channel_max_broken_time": {"customized": false, "type": "FloatPort", "value": 0.4}, "bad_channel_noise_threshold": {"customized": false, "type": "FloatPort", "value": 4}, "bad_window_removal_band": {"customized": false, "type": "ListPort", "value": []}, "burst_removal_cutoff": {"customized": false, "type": "FloatPort", "value": 10.0}, "calib_seconds": {"customized": false, "type": "IntPort", "value": 0}, "channels_to_import": {"customized": false, "type": "Port", "value": "all"}, "clean_signal_range": {"customized": false, "type": "ListPort", "value": [-4, 6]}, "desired_unit": {"customized": false, "type": "EnumPort", "value": "uV"}, "export_to_h5": {"customized": false, "type": "BoolPort", "value": false}, "extra_ar_params": {"customized": false, "type": "DictPort", "value": {}}, "fix_unit": {"customized": true, "type": "BoolPort", "value": true}, "highpass_frequencies": {"customized": true, "type": "ListPort", "value": [0.1, 0.2]}, "highpass_stop_atten": {"customized": false, "type": "FloatPort", "value": 50.0}, "init_on": {"customized": false, "type": "ListPort", "value": []}, "lowpass_frequencies": {"customized": true, "type": "ListPort", "value": [15, 16]}, "lowpass_stop_atten": {"customized": true, "type": "FloatPort", "value": 80}, "max_bad_channels": {"customized": false, "type": "FloatPort", "value": 0.2}, "max_broken_time": {"customized": false, "type": "FloatPort", "value": 0.4}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "montage": {"customized": false, "type": "EnumPort", "value": "auto"}, "notch_frequency": {"customized": true, "type": "FloatPort", "value": 50.0}, "num_samples": {"customized": true, "type": "IntPort", "value": 350}, "protected_channels_during_cleaning": {"customized": false, "type": "ListPort", "value": []}, "remove_unlocalized_chans": {"customized": false, "type": "BoolPort", "value": true}, "rereferencing": {"customized": false, "type": "Port", "value": "CAR"}, "sampling_rate": {"customized": false, "type": "FloatPort", "value": null}, "scale_factor": {"customized": false, "type": "FloatPort", "value": 1.0}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "skip_interpolate": {"customized": false, "type": "BoolPort", "value": false}, "skip_preprocessing": {"customized": false, "type": "BoolPort", "value": false}, "subset_size": {"customized": true, "type": "FloatPort", "value": 0.2}, "use_caching": {"customized": true, "type": "BoolPort", "value": true}, "use_clean_window": {"customized": false, "type": "BoolPort", "value": true}, "use_notch_filter": {"customized": false, "type": "BoolPort", "value": false}, "window_len": {"customized": false, "type": "FloatPort", "value": 0.5}}, "uuid": "03980fd6-f356-4134-859d-679754e3f91a"}, "node7": {"class": "EventRelatedPotential", "module": "neuropype.nodes.neural.EventRelatedPotential", "params": {"baseline_removal_range": {"customized": true, "type": "Port", "value": "-0.3...0"}, "channel_range": {"customized": false, "type": "Port", "value": ":"}, "lowpass_cutoff": {"customized": false, "type": "ListPort", "value": []}, "max_gap_length": {"customized": false, "type": "FloatPort", "value": 0.2}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "output_measure": {"customized": true, "type": "EnumPort", "value": "trials"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "skip_baseline_removal": {"customized": false, "type": "BoolPort", "value": false}, "time_bounds": {"customized": true, "type": "Port", "value": [-0.3, 1]}}, "uuid": "133e5ada-8c29-4c73-8bc3-8836e0b092a1"}, "node8": {"class": "GroupedMean", "module": "neuropype.nodes.statistics.GroupedMean", "params": {"allow_markers": {"customized": true, "type": "BoolPort", "value": false}, "ci_range": {"customized": false, "type": "FloatPort", "value": 0.95}, "ddof": {"customized": false, "type": "IntPort", "value": 1}, "equal_var": {"customized": false, "type": "BoolPort", "value": false}, "error_type": {"customized": false, "type": "EnumPort", "value": "none"}, "fill_cols": {"customized": false, "type": "BoolPort", "value": true}, "group_cols": {"customized": true, "type": "ListPort", "value": ["Marker"]}, "grouping_type": {"customized": false, "type": "EnumPort", "value": "levels"}, "mean_type": {"customized": false, "type": "EnumPort", "value": "mean"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": false, "type": "ListPort", "value": [0, 0]}, "use_caching": {"customized": false, "type": "BoolPort", "value": false}, "winsorize": {"customized": true, "type": "BoolPort", "value": false}}, "uuid": "4fbd6aaf-b263-4b16-9097-beee2e28291a"}, "node9": {"class": "SetStreamProperties", "module": "neuropype.nodes.utilities.SetStreamProperties", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "only_signals": {"customized": false, "type": "BoolPort", "value": false}, "properties": {"customized": true, "type": "DictPort", "value": {"has_markers": false}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}}, "uuid": "e07efee6-dc12-4cf5-ad5f-8d027fd2efbe"}}, "version": 1.1}</patch>
</scheme>
