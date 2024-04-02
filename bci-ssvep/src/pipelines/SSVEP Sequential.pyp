<?xml version='1.0' encoding='utf-8'?>
<scheme version="2.0" title="SSVEP Sequential" description="">
	<nodes>
		<node id="0" name="Import XDF" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" project_name="NeuroPype" version="1.4.3" title="Import XDF&#10;[C:/recordings/ssvep_sequenced_3/yegor_k/5_3__9_16_13_6s/yegor_k_ssvep_sequenced_3_2024-03-17_20-35-26_5_3__9_16_13_6s.xdf]" uuid="004217ea-5fd7-490a-836f-11d0367d5e34" position="(-709.9999999999999, 203.33333333333331)" />
		<node id="1" name="Set Axis Values" qualified_name="widgets.tensor_math.owsetaxisvalues.OWSetAxisValues" project_name="NeuroPype" version="1.0.2" title="Set Axis Values" uuid="9a539045-ca82-44cc-8733-2c67b181b136" position="(-518.3333333333335, 213.4444444444446)" />
		<node id="2" name="FIR Filter" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" project_name="NeuroPype" version="1.1.1" title="FIR Filter&#10;[[0.5, 1, 40, 45] Hz bandpass -50dB]" uuid="6ee31137-a2f5-45ad-a86c-f3ec6877183c" position="(-54.999999999999964, 113.44444444444451)" />
		<node id="3" name="Rewrite Markers" qualified_name="widgets.markers.owrewritemarkers.OWRewriteMarkers" project_name="NeuroPype" version="0.9.3" title="Rewrite Markers&#10;[{'trial-start-16-hz': 'target-trial-begin', 'trial...]" uuid="842ed4cd-1b15-4fb4-9789-57941d7ebcd0" position="(-201.66666666666669, 112.33333333333346)" />
		<node id="4" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.4.0" title="Select Range&#10;[5:20 along frequency (Hz)]" uuid="8fa221db-060a-4114-8068-a165baf2dadf" position="(608.5555555555555, 289.44444444444446)" />
		<node id="5" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.4.0" title="Select Range&#10;[['Oz'] along space (names)]" uuid="eb1967eb-39ad-4de1-aa58-bf2a55b9728e" position="(408.3333333333335, 289.0000000000001)" />
		<node id="6" name="Insert Markers" qualified_name="widgets.markers.owinsertmarkers.OWInsertMarkers" project_name="NeuroPype" version="1.3.0" title="Insert Markers" uuid="a2aa597b-2938-47eb-bd62-94b2e8e7f464" position="(103.88888888888893, 114.44444444444443)" />
		<node id="7" name="Segmentation" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" project_name="NeuroPype" version="1.0.2" title="Segmentation" uuid="15dc8f21-4079-4d0c-953f-b5c6b0bd046f" position="(228.3333333333332, 290.11111111111103)" />
		<node id="8" name="Inspect Packet" qualified_name="widgets.visualization.owinspectpacket.OWInspectPacket" project_name="NeuroPype" version="3.1.0" title="Inspect Packet&#10;[time x space]" uuid="f3764eda-d7b3-41de-9547-e83f17880823" position="(-529.5555555555552, 96.77777777777777)" />
		<node id="9" name="Export to CSV" qualified_name="widgets.file_system.owexportcsv.OWExportCSV" project_name="NeuroPype" version="1.2.1   " title="Export to CSV&#10;[columns from time, frows from instance, saving to 16hz.csv under C:/Users/Kiril/Desktop/huinya 2/python/cca/data]" uuid="ca34f1d9-2a7b-4e95-a4e0-8fbb4803704f" position="(765.6666666666666, 425.2222222222222)" />
		<node id="10" name="Hold Last Packet" qualified_name="widgets.utilities.owholdlastpacket.OWHoldLastPacket" project_name="NeuroPype" version="1.0.0" title="Hold Last Packet" uuid="a61388b7-513a-4aa3-b51e-f631eb908f3a" position="(-378.88888888888863, 212.2222222222222)" />
		<node id="11" name="Break Structure / Dict" qualified_name="widgets.programming.owbreakstructure.OWBreakStructure" project_name="NeuroPype" version="1.0.0" title="Break Structure / Dict&#10;[rule,name]" uuid="62e43a79-6288-46c9-bfec-a295cc1a57bc" position="(-316.6666666666668, 461.1111111111109)" />
		<node id="12" name="List Iterator" qualified_name="widgets.programming.owlistiterator.OWListIterator" project_name="NeuroPype" version="1.2.0" title="List Iterator" uuid="32bb35a8-4169-47ec-ae9e-af5c47690e16" position="(-468.88888888888897, 463.3333333333333)" />
		<node id="13" name="Parameter Port" qualified_name="widgets.programming.owparameterport.OWParameterPort" project_name="NeuroPype" version="1.3.3" title="Parameter Port&#10;[data (dict)]" uuid="9b2549d3-0747-4b17-9596-ed889acafd54" position="(-1330.1111111111113, 324.11111111111126)" />
		<node id="14" name="Break Structure / Dict" qualified_name="widgets.programming.owbreakstructure.OWBreakStructure" project_name="NeuroPype" version="1.0.0" title="Break Structure / Dict&#10;[filename,hz,secs,path]" uuid="133ad7eb-a2a5-4437-ad95-218e37d6eeda" position="(-1146.1111111111104, 326.4333333333332)" />
	</nodes>
	<links>
		<link id="0" source_node_id="3" sink_node_id="2" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="1" source_node_id="5" sink_node_id="4" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="2" source_node_id="0" sink_node_id="1" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="3" source_node_id="6" sink_node_id="7" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="4" source_node_id="0" sink_node_id="8" source_channel="Data" sink_channel="Data" enabled="false" />
		<link id="5" source_node_id="7" sink_node_id="5" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="6" source_node_id="4" sink_node_id="9" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="7" source_node_id="1" sink_node_id="10" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="8" source_node_id="10" sink_node_id="3" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="9" source_node_id="11" sink_node_id="3" source_channel="Out0" sink_channel="Rewriting Rule" enabled="true" />
		<link id="10" source_node_id="11" sink_node_id="9" source_channel="Out1" sink_channel="Filename" enabled="true" />
		<link id="11" source_node_id="2" sink_node_id="6" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="12" source_node_id="12" sink_node_id="11" source_channel="Curitem" sink_channel="Indict" enabled="true" />
		<link id="13" source_node_id="13" sink_node_id="14" source_channel="Value" sink_channel="Indict" enabled="true" />
		<link id="14" source_node_id="14" sink_node_id="0" source_channel="Out0" sink_channel="Filename" enabled="true" />
		<link id="15" source_node_id="14" sink_node_id="12" source_channel="Out1" sink_channel="Items To Iterate Over" enabled="true" />
		<link id="16" source_node_id="14" sink_node_id="7" source_channel="Out2" sink_channel="Segment Time Limits" enabled="true" />
		<link id="17" source_node_id="14" sink_node_id="9" source_channel="Out3" sink_channel="Output Root" enabled="true" />
	</links>
	<annotations>
		<text id="0" rect="(-576.4444444444443, -84.66666666666659, 584.0, 88.0)" font-family="Helvetica" font-size="16">{'trial-start-14-hz': 'target-trial-begin', 'trial-end-14-hz': 'target-trial-end'}
{'trial-start-15-hz': 'target-trial-begin', 'trial-end-15-hz': 'target-trial-end'}
{'trial-start-16-hz': 'target-trial-begin', 'trial-end-16-hz': 'target-trial-end'}</text>
		<arrow id="1" start="(-211.99999999999997, -14.222222222222214)" end="(-204.22222222222217, 60.0)" fill="#C1272D" />
	</annotations>
	<thumbnail />
	<node_properties>
		<properties node_id="0" format="pickle">gASVTgIAAAAAAAB9lCiMDWNsb3VkX2FjY291bnSUjACUjAxjbG91ZF9idWNrZXSUaAKMEWNsb3Vk
X2NyZWRlbnRpYWxzlGgCjApjbG91ZF9ob3N0lIwHRGVmYXVsdJSMCGZpbGVuYW1llIx5QzovcmVj
b3JkaW5ncy9zc3ZlcF9zZXF1ZW5jZWRfMy95ZWdvcl9rLzVfM19fOV8xNl8xM182cy95ZWdvcl9r
X3NzdmVwX3NlcXVlbmNlZF8zXzIwMjQtMDMtMTdfMjAtMzUtMjZfNV8zX185XzE2XzEzXzZzLnhk
ZpSME2hhbmRsZV9jbG9ja19yZXNldHOUiIwRaGFuZGxlX2Nsb2NrX3N5bmOUiIwVaGFuZGxlX2pp
dHRlcl9yZW1vdmFslIiMDm1heF9tYXJrZXJfbGVulIwNKHVzZSBkZWZhdWx0KZSMCG1ldGFkYXRh
lH2UjBJyZW9yZGVyX3RpbWVzdGFtcHOUiYwOcmV0YWluX3N0cmVhbXOUaA2ME3NhdmVkV2lkZ2V0
R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVB
cnJheZRDQgHZ0MsAAwAAAAADCwAAANcAAAR0AAADGwAAAwwAAAD2AAAEcwAAAxoAAAAAAAAAAAeA
AAADDAAAAPYAAARzAAADGpSFlIeUUpSMDnNldF9icmVha3BvaW50lImMC3VzZV9jYWNoaW5nlImM
D3VzZV9zdHJlYW1uYW1lc5SJjAd2ZXJib3NllIl1Lg==
</properties>
		<properties node_id="1" format="pickle">gASV2QEAAAAAAAB9lCiMCmFycmF5X25hbWWUjA0odXNlIGRlZmF1bHQplIwEYXhpc5SMBXNwYWNl
lIwKYXhpc19sYWJlbJSMDSh1c2UgZGVmYXVsdCmUjA9heGlzX29jY3VycmVuY2WUSwCMD2hhbmRs
ZV9leGlzdGluZ5SMC3JlcGxhY2UtYWxslIwSaW5mZXJfZHVtbXlfdmFsdWVzlImMCG1ldGFkYXRh
lH2UjAxvbmx5X3NpZ25hbHOUiIwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSMA3NpcJSMDl91bnBpY2ts
ZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAAMLAAAA5wAA
BHQAAAMLAAADDAAAAQYAAARzAAADCgAAAAAAAAAAB4AAAAMMAAABBgAABHMAAAMKlIWUh5RSlIwO
c2V0X2JyZWFrcG9pbnSUiYwGc3RyZWFtlIwNKHVzZSBkZWZhdWx0KZSMBnZhbHVlc5RdlCiMA2Zw
MZSMA2ZwMpSMA3BvM5SMA3BvNJSMAm8xlIwCbzKUjANwbzWUjANwbzaUjAJmN5SMAmY4lIwCQ3qU
jAJGepSMAlB6lIwCT3qUjAJwM5SMAnA0lGV1Lg==
</properties>
		<properties node_id="2" format="pickle">gASVkwEAAAAAAAB9lCiMDWFudGlzeW1tZXRyaWOUiYwEYXhpc5SMBHRpbWWUjBJjb252b2x1dGlv
bl9tZXRob2SUjAhzdGFuZGFyZJSMDmN1dF9wcmVyaW5naW5nlImMCWRpcmVjdGlvbpSMB2Zvcndh
cmSUjAtmcmVxdWVuY2llc5RdlChHP+AAAAAAAABLAUsoSy1ljAhtZXRhZGF0YZR9lIwNbWluaW11
bV9waGFzZZSIjARtb2RllIwIYmFuZHBhc3OUjAVvcmRlcpSMDSh1c2UgZGVmYXVsdCmUjBNzYXZl
ZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSM
ClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAq0AAAB7AAAEFgAAAzEAAAKuAAAAmgAABBUAAAMwAAAA
AAAAAAAHgAAAAq4AAACaAAAEFQAAAzCUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjApzdG9wX2F0
dGVulEdASQAAAAAAAHUu
</properties>
		<properties node_id="3" format="pickle">gASVawEAAAAAAAB9lCiMCWl2X2NvbHVtbpSMBk1hcmtlcpSMCG1ldGFkYXRhlH2UjA5wYXR0ZXJu
X3N5bnRheJSMCXdpbGRjYXJkc5SMCXJlZ2V4X3N1YpSJjBFyZW1vdmVfYWxsX290aGVyc5SIjAVy
dWxlc5SMUnsndHJpYWwtc3RhcnQtMTYtaHonOiAndGFyZ2V0LXRyaWFsLWJlZ2luJywgJ3RyaWFs
LWVuZC0xNi1oeic6ICd0YXJnZXQtdHJpYWwtZW5kJ32UjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwD
c2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDL
AAMAAAAAAwsAAAFYAAAEdAAAApkAAAMMAAABdwAABHMAAAKYAAAAAAAAAAAHgAAAAwwAAAF3AAAE
cwAAApiUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJdS4=
</properties>
		<properties node_id="4" format="pickle">gASVJgEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwJZnJlcXVlbmN5lIwIbWV0YWRhdGGUfZSME3NhdmVkV2lk
Z2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5
dGVBcnJheZRDQgHZ0MsAAwAAAAAESwAAAiYAAAW0AAADMwAABEwAAAJFAAAFswAAAzIAAAAAAAAA
AAoAAAAETAAAAkUAAAWzAAADMpSFlIeUUpSMCXNlbGVjdGlvbpSMBDU6MjCUjA5zZXRfYnJlYWtw
b2ludJSJjAR1bml0lIwCSHqUdS4=
</properties>
		<properties node_id="5" format="pickle">gASVJgEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwFc3BhY2WUjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAARLAAAB4wAABbQAAAN2AAAETAAAAgIAAAWzAAADdQAAAAAAAAAACgAA
AARMAAACAgAABbMAAAN1lIWUh5RSlIwJc2VsZWN0aW9ulF2UjAJPepRhjA5zZXRfYnJlYWtwb2lu
dJSJjAR1bml0lIwFbmFtZXOUdS4=
</properties>
		<properties node_id="6" format="pickle">gASVhgIAAAAAAAB9lCiMDWFuY2hvcl9tYXJrZXKUjBJ0YXJnZXQtdHJpYWwtYmVnaW6UjA9hbmNo
b3JfbWFya2VyX0KUjBB0YXJnZXQtdHJpYWwtZW5klIwFY291bnSUSwSMCGNvdW50aW5nlIwJcGVy
c2Vjb25klIwXZW5mb3JjZV9pbnRlcm1pdHRlbnRfaW6UjAttYXJrZXItc3BhbpSMDmV4Y2VwdF9t
YXJrZXJzlF2UjAxleHRyYV9saW1pdHOUXZSMFGluc3RhbmNlX2ZpZWxkc19mcm9tlIwFZmlyc3SU
jBRpbnRlcm1pdHRlbnRfbWFya2Vyc5SMBWFsbG93lIwNbWFya2VyX2Zvcm1hdJSMCHZlcmJhdGlt
lIwVbWFya2VyX2xvY2tlZF9pbmRpY2VzlF2UjAptYXhfbGVuZ3RolIwNKHVzZSBkZWZhdWx0KZSM
CG1ldGFkYXRhlH2UjAptaW5fbGVuZ3RolGgXjARtb2RllIwObWFya2VyLXNwYW5uZWSUjAdwYXls
b2FklIwQdGFyZ2V0LWZmdC1zdGFydJSMCXBsYWNlbWVudJSMC2VxdWlkaXN0YW50lIwLcmFuZG9t
X3NlZWSUTTkwjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SM
DFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAukAAAC9AAAElgAAA1IAAALp
AAAAvQAABJYAAANSAAAAAAAAAAAHgAAAAukAAAC9AAAElgAAA1KUhZSHlFKUjA5zZXRfYnJlYWtw
b2ludJSJjAt0aW1lX2xpbWl0c5RdlChLAEsAZXUu
</properties>
		<properties node_id="7" format="pickle">gASVbgEAAAAAAAB9lCiMEWtlZXBfbWFya2VyX2NodW5rlImMDm1heF9nYXBfbGVuZ3RolEc/yZmZ
mZmZmowIbWV0YWRhdGGUfZSMD29ubGluZV9lcG9jaGluZ5SMDW1hcmtlci1sb2NrZWSUjA1zYW1w
bGVfb2Zmc2V0lEsAjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWU
k5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAwwAAAEgAAAEcwAAAvAA
AAMMAAABIAAABHMAAALwAAAAAAAAAAAHgAAAAwwAAAEgAAAEcwAAAvCUhZSHlFKUjA5zZWxlY3Rf
bWFya2Vyc5RdlIwSdGFyZ2V0LXRyaWFsLWJlZ2lulGGMDnNldF9icmVha3BvaW50lImMC3RpbWVf
Ym91bmRzlF2UKEc/weuFHrhR7EsGZYwHdmVyYm9zZZSJdS4=
</properties>
		<properties node_id="8" format="literal">{'always_on_top': True, 'col_axis': 'time', 'decimals': 6, 'every_n_ticks': 1, 'fewer_buttons': False, 'font_size': 10, 'ignore_signal_changes': False, 'initial_position': [20, 20, 800, 800], 'metadata': {}, 'row_axis': 'space', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'show_axes_table': True, 'show_data_table': True, 'show_markers_table': False, 'show_max_columns': 20, 'show_max_values': 50, 'show_streams_table': False, 'stream': '(use default)', 'stream_name': '(use default)', 'verbose': True, 'window_title': 'Inspect Data Packet'}</properties>
		<properties node_id="9" format="pickle">gASVvQEAAAAAAAB9lCiMEGF4aXNfZGVzY3JpcHRpb26UjACUjA1jbG91ZF9hY2NvdW50lGgCjAxj
bG91ZF9idWNrZXSUaAKMEWNsb3VkX2NyZWRlbnRpYWxzlGgCjApjbG91ZF9ob3N0lIwHRGVmYXVs
dJSMCGNvbF9heGlzlIwEdGltZZSMDWNvbHVtbl9oZWFkZXKUiIwIZmlsZW5hbWWUjAgxNmh6LmNz
dpSMCG1ldGFkYXRhlH2UjAtvdXRwdXRfcm9vdJSML0M6L1VzZXJzL0tpcmlsL0Rlc2t0b3AvaHVp
bnlhIDIvcHl0aG9uL2NjYS9kYXRhlIwIcm93X2F4aXOUjAhpbnN0YW5jZZSMCnJvd19oZWFkZXKU
iIwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5R
dENvcmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAARLAAABgQAABbQAAAPZAAAETAAAAaAAAAWz
AAAD2AAAAAAAAAAACgAAAARMAAABoAAABbMAAAPYlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiXUu
</properties>
		<properties node_id="10" format="pickle">gASVugAAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwO
X3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAA
AwsAAAHAAAAEdAAAAjEAAAMMAAAB3wAABHMAAAIwAAAAAAAAAAAHgAAAAwwAAAHfAAAEcwAAAjCU
hZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJdS4=
</properties>
		<properties node_id="11" format="pickle">gASVxQMAAAAAAAB9lCiMCGRlZmF1bHQwlIwNKHVzZSBkZWZhdWx0KZSMCGRlZmF1bHQxlIwNKHVz
ZSBkZWZhdWx0KZSMCWRlZmF1bHQxMJSMDSh1c2UgZGVmYXVsdCmUjAlkZWZhdWx0MTGUjA0odXNl
IGRlZmF1bHQplIwJZGVmYXVsdDEylIwNKHVzZSBkZWZhdWx0KZSMCWRlZmF1bHQxM5SMDSh1c2Ug
ZGVmYXVsdCmUjAlkZWZhdWx0MTSUjA0odXNlIGRlZmF1bHQplIwIZGVmYXVsdDKUjA0odXNlIGRl
ZmF1bHQplIwIZGVmYXVsdDOUjA0odXNlIGRlZmF1bHQplIwIZGVmYXVsdDSUjA0odXNlIGRlZmF1
bHQplIwIZGVmYXVsdDWUjA0odXNlIGRlZmF1bHQplIwIZGVmYXVsdDaUjA0odXNlIGRlZmF1bHQp
lIwIZGVmYXVsdDeUjA0odXNlIGRlZmF1bHQplIwIZGVmYXVsdDiUjA0odXNlIGRlZmF1bHQplIwI
ZGVmYXVsdDmUjA0odXNlIGRlZmF1bHQplIwNZGVmYXVsdHNfdHlwZZSMA3N0cpSMCG1ldGFkYXRh
lH2UjAVuYW1lMJSMBHJ1bGWUjAVuYW1lMZSMBG5hbWWUjAZuYW1lMTCUjA0odXNlIGRlZmF1bHQp
lIwGbmFtZTExlIwNKHVzZSBkZWZhdWx0KZSMBm5hbWUxMpSMDSh1c2UgZGVmYXVsdCmUjAZuYW1l
MTOUjA0odXNlIGRlZmF1bHQplIwGbmFtZTE0lIwNKHVzZSBkZWZhdWx0KZSMBW5hbWUylIwNKHVz
ZSBkZWZhdWx0KZSMBW5hbWUzlIwNKHVzZSBkZWZhdWx0KZSMBW5hbWU0lIwNKHVzZSBkZWZhdWx0
KZSMBW5hbWU1lIwNKHVzZSBkZWZhdWx0KZSMBW5hbWU2lIwNKHVzZSBkZWZhdWx0KZSMBW5hbWU3
lIwNKHVzZSBkZWZhdWx0KZSMBW5hbWU4lIwNKHVzZSBkZWZhdWx0KZSMBW5hbWU5lIwNKHVzZSBk
ZWZhdWx0KZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwM
UHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAADCwAAAJ4AAAR0AAADUwAAAwwA
AAC9AAAEcwAAA1IAAAAAAAAAAAeAAAADDAAAAL0AAARzAAADUpSFlIeUUpSMDnNldF9icmVha3Bv
aW50lIl1Lg==
</properties>
		<properties node_id="12" format="pickle">gASVzwAAAAAAAAB9lCiMBWl0ZW1zlF2UjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRHZW9tZXRy
eZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFycmF5lENC
AdnQywADAAAAAAMLAAABfgAABHQAAAJ0AAADDAAAAZ0AAARzAAACcwAAAAAAAAAAB4AAAAMMAAAB
nQAABHMAAAJzlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwHdmVyYm9zZZSJdS4=
</properties>
		<properties node_id="13" format="pickle">gASVygEAAAAAAAB9lCiMCGF1dG9jYXN0lIiMCWNhbmJlbm9uZZSIjAdkZWZhdWx0lIwAlIwEZGVz
Y5RoBIwGZG9tYWlulIwNKHVzZSBkZWZhdWx0KZSMCGVkaXRhYmxllIiMBmV4cGVydJSJjAtpc19m
aWxlbmFtZZSJjAppc192aXNpYmxllIiMCG1ldGFkYXRhlH2UjA1wb3J0X2NhdGVnb3J5lGgEjAhw
b3J0bmFtZZSMBGRhdGGUjA1yZWxhdGlvbnNoaXBzlF2UjARzYWZllImME3NhdmVkV2lkZ2V0R2Vv
bWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJh
eZRDQgHZ0MsAAwAAAAADCwAAAJ4AAAR0AAADUwAAAwwAAAC9AAAEcwAAA1IAAAAAAAAAAAeAAAAD
DAAAAL0AAARzAAADUpSFlIeUUpSMBnNlbGVjdJSMBG5vbmWUjBNzZW5kX3NpZ25hbF9jaGFuZ2Vk
lIiMDnNldF9icmVha3BvaW50lImMCnZhbHVlX3R5cGWUjARkaWN0lIwHdmVyYm9zZZSJjAx2ZXJi
b3NlX25hbWWUaAd1Lg==
</properties>
		<properties node_id="14" format="pickle">gASVVwIAAAAAAAB9lCiMCGRlZmF1bHQwlIwNKHVzZSBkZWZhdWx0KZSMCGRlZmF1bHQxlGgCjAlk
ZWZhdWx0MTCUaAKMCWRlZmF1bHQxMZRoAowJZGVmYXVsdDEylGgCjAlkZWZhdWx0MTOUaAKMCWRl
ZmF1bHQxNJRoAowIZGVmYXVsdDKUaAKMCGRlZmF1bHQzlGgCjAhkZWZhdWx0NJRoAowIZGVmYXVs
dDWUaAKMCGRlZmF1bHQ2lGgCjAhkZWZhdWx0N5RoAowIZGVmYXVsdDiUaAKMCGRlZmF1bHQ5lGgC
jA1kZWZhdWx0c190eXBllIwDc3RylIwIbWV0YWRhdGGUfZSMBW5hbWUwlIwIZmlsZW5hbWWUjAVu
YW1lMZSMAmh6lIwGbmFtZTEwlGgCjAZuYW1lMTGUaAKMBm5hbWUxMpRoAowGbmFtZTEzlGgCjAZu
YW1lMTSUaAKMBW5hbWUylIwEc2Vjc5SMBW5hbWUzlIwEcGF0aJSMBW5hbWU0lGgCjAVuYW1lNZRo
AowFbmFtZTaUaAKMBW5hbWU3lGgCjAVuYW1lOJRoAowFbmFtZTmUaAKME3NhdmVkV2lkZ2V0R2Vv
bWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJh
eZRDQgHZ0MsAAwAAAAADUwAAATcAAAS8AAAD7AAAA1QAAAFWAAAEuwAAA+sAAAAAAAAAAAeAAAAD
VAAAAVYAAAS7AAAD65SFlIeUUpSMDnNldF9icmVha3BvaW50lIl1Lg==
</properties>
	</node_properties>
	<patch>{"description": {"description": "", "license": "", "name": "SSVEP Sequential", "status": "(unspecified)", "url": "", "version": "0.0.0"}, "edges": [["node4", "data", "node3", "data"], ["node6", "data", "node5", "data"], ["node1", "data", "node2", "data"], ["node7", "data", "node8", "data"], ["node8", "data", "node6", "data"], ["node5", "data", "node10", "data"], ["node2", "data", "node11", "data"], ["node11", "data", "node4", "data"], ["node12", "out0", "node4", "rules"], ["node12", "out1", "node10", "filename"], ["node3", "data", "node7", "data"], ["node13", "curitem", "node12", "indict"], ["node14", "value", "node15", "indict"], ["node15", "out0", "node1", "filename"], ["node15", "out1", "node13", "items"], ["node15", "out2", "node8", "time_bounds"], ["node15", "out3", "node10", "output_root"]], "nodes": {"node1": {"class": "ImportXDF", "module": "neuropype.nodes.file_system.ImportXDF", "params": {"cloud_account": {"customized": false, "type": "StringPort", "value": ""}, "cloud_bucket": {"customized": false, "type": "StringPort", "value": ""}, "cloud_credentials": {"customized": false, "type": "StringPort", "value": ""}, "cloud_host": {"customized": false, "type": "EnumPort", "value": "Default"}, "filename": {"customized": true, "type": "StringPort", "value": "C:/recordings/ssvep_sequenced_3/yegor_k/5_3__9_16_13_6s/yegor_k_ssvep_sequenced_3_2024-03-17_20-35-26_5_3__9_16_13_6s.xdf"}, "handle_clock_resets": {"customized": false, "type": "BoolPort", "value": true}, "handle_clock_sync": {"customized": false, "type": "BoolPort", "value": true}, "handle_jitter_removal": {"customized": false, "type": "BoolPort", "value": true}, "max_marker_len": {"customized": false, "type": "IntPort", "value": null}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "reorder_timestamps": {"customized": false, "type": "BoolPort", "value": false}, "retain_streams": {"customized": false, "type": "Port", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "use_caching": {"customized": false, "type": "BoolPort", "value": false}, "use_streamnames": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "004217ea-5fd7-490a-836f-11d0367d5e34"}, "node10": {"class": "ExportCSV", "module": "neuropype.nodes.file_system.ExportCSV", "params": {"axis_description": {"customized": false, "type": "StringPort", "value": ""}, "cloud_account": {"customized": false, "type": "StringPort", "value": ""}, "cloud_bucket": {"customized": false, "type": "StringPort", "value": ""}, "cloud_credentials": {"customized": false, "type": "StringPort", "value": ""}, "cloud_host": {"customized": false, "type": "EnumPort", "value": "Default"}, "col_axis": {"customized": true, "type": "ComboPort", "value": "time"}, "column_header": {"customized": false, "type": "BoolPort", "value": true}, "filename": {"customized": true, "type": "StringPort", "value": "16hz.csv"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "output_root": {"customized": true, "type": "StringPort", "value": "C:/Users/Kiril/Desktop/huinya 2/python/cca/data"}, "row_axis": {"customized": true, "type": "ComboPort", "value": "instance"}, "row_header": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "ca34f1d9-2a7b-4e95-a4e0-8fbb4803704f"}, "node11": {"class": "HoldLastPacket", "module": "neuropype.nodes.utilities.HoldLastPacket", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "a61388b7-513a-4aa3-b51e-f631eb908f3a"}, "node12": {"class": "BreakStructure", "module": "neuropype.nodes.programming.BreakStructure", "params": {"default0": {"customized": false, "type": "Port", "value": null}, "default1": {"customized": false, "type": "Port", "value": null}, "default10": {"customized": false, "type": "Port", "value": null}, "default11": {"customized": false, "type": "Port", "value": null}, "default12": {"customized": false, "type": "Port", "value": null}, "default13": {"customized": false, "type": "Port", "value": null}, "default14": {"customized": false, "type": "Port", "value": null}, "default2": {"customized": false, "type": "Port", "value": null}, "default3": {"customized": false, "type": "Port", "value": null}, "default4": {"customized": false, "type": "Port", "value": null}, "default5": {"customized": false, "type": "Port", "value": null}, "default6": {"customized": false, "type": "Port", "value": null}, "default7": {"customized": false, "type": "Port", "value": null}, "default8": {"customized": false, "type": "Port", "value": null}, "default9": {"customized": false, "type": "Port", "value": null}, "defaults_type": {"customized": false, "type": "EnumPort", "value": "str"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "name0": {"customized": true, "type": "StringPort", "value": "rule"}, "name1": {"customized": true, "type": "StringPort", "value": "name"}, "name10": {"customized": false, "type": "StringPort", "value": null}, "name11": {"customized": false, "type": "StringPort", "value": null}, "name12": {"customized": false, "type": "StringPort", "value": null}, "name13": {"customized": false, "type": "StringPort", "value": null}, "name14": {"customized": false, "type": "StringPort", "value": null}, "name2": {"customized": false, "type": "StringPort", "value": null}, "name3": {"customized": false, "type": "StringPort", "value": null}, "name4": {"customized": false, "type": "StringPort", "value": null}, "name5": {"customized": false, "type": "StringPort", "value": null}, "name6": {"customized": false, "type": "StringPort", "value": null}, "name7": {"customized": false, "type": "StringPort", "value": null}, "name8": {"customized": false, "type": "StringPort", "value": null}, "name9": {"customized": false, "type": "StringPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "62e43a79-6288-46c9-bfec-a295cc1a57bc"}, "node13": {"class": "ListIterator", "module": "neuropype.nodes.programming.ListIterator", "params": {"items": {"customized": false, "type": "ListPort", "value": []}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "32bb35a8-4169-47ec-ae9e-af5c47690e16"}, "node14": {"class": "ParameterPort", "module": "neuropype.nodes.programming.ParameterPort", "params": {"autocast": {"customized": false, "type": "BoolPort", "value": true}, "canbenone": {"customized": false, "type": "BoolPort", "value": true}, "default": {"customized": false, "type": "Port", "value": ""}, "desc": {"customized": false, "type": "StringPort", "value": ""}, "domain": {"customized": false, "type": "Port", "value": null}, "editable": {"customized": false, "type": "BoolPort", "value": true}, "expert": {"customized": false, "type": "BoolPort", "value": false}, "is_filename": {"customized": false, "type": "BoolPort", "value": false}, "is_visible": {"customized": false, "type": "BoolPort", "value": true}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "port_category": {"customized": false, "type": "StringPort", "value": ""}, "portname": {"customized": false, "type": "StringPort", "value": "data"}, "relationships": {"customized": false, "type": "ListPort", "value": []}, "safe": {"customized": false, "type": "BoolPort", "value": false}, "select": {"customized": false, "type": "EnumPort", "value": "none"}, "send_signal_changed": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "value_type": {"customized": true, "type": "EnumPort", "value": "dict"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "verbose_name": {"customized": false, "type": "StringPort", "value": null}}, "uuid": "9b2549d3-0747-4b17-9596-ed889acafd54"}, "node15": {"class": "BreakStructure", "module": "neuropype.nodes.programming.BreakStructure", "params": {"default0": {"customized": false, "type": "Port", "value": null}, "default1": {"customized": false, "type": "Port", "value": null}, "default10": {"customized": false, "type": "Port", "value": null}, "default11": {"customized": false, "type": "Port", "value": null}, "default12": {"customized": false, "type": "Port", "value": null}, "default13": {"customized": false, "type": "Port", "value": null}, "default14": {"customized": false, "type": "Port", "value": null}, "default2": {"customized": false, "type": "Port", "value": null}, "default3": {"customized": false, "type": "Port", "value": null}, "default4": {"customized": false, "type": "Port", "value": null}, "default5": {"customized": false, "type": "Port", "value": null}, "default6": {"customized": false, "type": "Port", "value": null}, "default7": {"customized": false, "type": "Port", "value": null}, "default8": {"customized": false, "type": "Port", "value": null}, "default9": {"customized": false, "type": "Port", "value": null}, "defaults_type": {"customized": false, "type": "EnumPort", "value": "str"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "name0": {"customized": true, "type": "StringPort", "value": "filename"}, "name1": {"customized": true, "type": "StringPort", "value": "hz"}, "name10": {"customized": false, "type": "StringPort", "value": null}, "name11": {"customized": false, "type": "StringPort", "value": null}, "name12": {"customized": false, "type": "StringPort", "value": null}, "name13": {"customized": false, "type": "StringPort", "value": null}, "name14": {"customized": false, "type": "StringPort", "value": null}, "name2": {"customized": true, "type": "StringPort", "value": "secs"}, "name3": {"customized": true, "type": "StringPort", "value": "path"}, "name4": {"customized": false, "type": "StringPort", "value": null}, "name5": {"customized": false, "type": "StringPort", "value": null}, "name6": {"customized": false, "type": "StringPort", "value": null}, "name7": {"customized": false, "type": "StringPort", "value": null}, "name8": {"customized": false, "type": "StringPort", "value": null}, "name9": {"customized": false, "type": "StringPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "133ad7eb-a2a5-4437-ad95-218e37d6eeda"}, "node2": {"class": "SetAxisValues", "module": "neuropype.nodes.tensor_math.SetAxisValues", "params": {"array_name": {"customized": false, "type": "StringPort", "value": null}, "axis": {"customized": true, "type": "ComboPort", "value": "space"}, "axis_label": {"customized": false, "type": "StringPort", "value": null}, "axis_occurrence": {"customized": false, "type": "IntPort", "value": 0}, "handle_existing": {"customized": false, "type": "EnumPort", "value": "replace-all"}, "infer_dummy_values": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "only_signals": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stream": {"customized": false, "type": "StringPort", "value": null}, "values": {"customized": true, "type": "Port", "value": ["fp1", "fp2", "po3", "po4", "o1", "o2", "po5", "po6", "f7", "f8", "Cz", "Fz", "Pz", "Oz", "p3", "p4"]}}, "uuid": "9a539045-ca82-44cc-8733-2c67b181b136"}, "node3": {"class": "FIRFilter", "module": "neuropype.nodes.signal_processing.FIRFilter", "params": {"antisymmetric": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": false, "type": "ComboPort", "value": "time"}, "convolution_method": {"customized": false, "type": "EnumPort", "value": "standard"}, "cut_preringing": {"customized": false, "type": "BoolPort", "value": false}, "direction": {"customized": false, "type": "EnumPort", "value": "forward"}, "frequencies": {"customized": true, "type": "ListPort", "value": [0.5, 1, 40, 45]}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "minimum_phase": {"customized": false, "type": "BoolPort", "value": true}, "mode": {"customized": false, "type": "EnumPort", "value": "bandpass"}, "order": {"customized": false, "type": "IntPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stop_atten": {"customized": false, "type": "FloatPort", "value": 50.0}}, "uuid": "6ee31137-a2f5-45ad-a86c-f3ec6877183c"}, "node4": {"class": "RewriteMarkers", "module": "neuropype.nodes.markers.RewriteMarkers", "params": {"iv_column": {"customized": false, "type": "StringPort", "value": "Marker"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "pattern_syntax": {"customized": false, "type": "EnumPort", "value": "wildcards"}, "regex_sub": {"customized": false, "type": "BoolPort", "value": false}, "remove_all_others": {"customized": true, "type": "BoolPort", "value": true}, "rules": {"customized": true, "type": "Port", "value": "{'trial-start-16-hz': 'target-trial-begin', 'trial-end-16-hz': 'target-trial-end'}"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "842ed4cd-1b15-4fb4-9789-57941d7ebcd0"}, "node5": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "ComboPort", "value": "frequency"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": "5:20"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "Hz"}}, "uuid": "8fa221db-060a-4114-8068-a165baf2dadf"}, "node6": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "ComboPort", "value": "space"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": ["Oz"]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "names"}}, "uuid": "eb1967eb-39ad-4de1-aa58-bf2a55b9728e"}, "node7": {"class": "InsertMarkers", "module": "neuropype.nodes.markers.InsertMarkers", "params": {"anchor_marker": {"customized": true, "type": "Port", "value": "target-trial-begin"}, "anchor_marker_B": {"customized": true, "type": "Port", "value": "target-trial-end"}, "count": {"customized": true, "type": "FloatPort", "value": 4.0}, "counting": {"customized": true, "type": "EnumPort", "value": "persecond"}, "enforce_intermittent_in": {"customized": false, "type": "EnumPort", "value": "marker-span"}, "except_markers": {"customized": false, "type": "ListPort", "value": []}, "extra_limits": {"customized": false, "type": "ListPort", "value": []}, "instance_fields_from": {"customized": false, "type": "EnumPort", "value": "first"}, "intermittent_markers": {"customized": false, "type": "EnumPort", "value": "allow"}, "marker_format": {"customized": false, "type": "EnumPort", "value": "verbatim"}, "marker_locked_indices": {"customized": false, "type": "ListPort", "value": []}, "max_length": {"customized": false, "type": "FloatPort", "value": null}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "min_length": {"customized": false, "type": "FloatPort", "value": null}, "mode": {"customized": true, "type": "EnumPort", "value": "marker-spanned"}, "payload": {"customized": true, "type": "Port", "value": "target-fft-start"}, "placement": {"customized": false, "type": "EnumPort", "value": "equidistant"}, "random_seed": {"customized": false, "type": "IntPort", "value": 12345}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "time_limits": {"customized": true, "type": "ListPort", "value": [0, 0]}}, "uuid": "a2aa597b-2938-47eb-bd62-94b2e8e7f464"}, "node8": {"class": "Segmentation", "module": "neuropype.nodes.formatting.Segmentation", "params": {"keep_marker_chunk": {"customized": false, "type": "BoolPort", "value": false}, "max_gap_length": {"customized": false, "type": "FloatPort", "value": 0.2}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "online_epoching": {"customized": false, "type": "EnumPort", "value": "marker-locked"}, "sample_offset": {"customized": false, "type": "IntPort", "value": 0}, "select_markers": {"customized": true, "type": "ListPort", "value": ["target-trial-begin"]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "time_bounds": {"customized": true, "type": "ListPort", "value": [0.14, 6]}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "15dc8f21-4079-4d0c-953f-b5c6b0bd046f"}, "node9": {"class": "InspectPacket", "module": "neuropype.nodes.visualization.InspectPacket", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": true}, "col_axis": {"customized": false, "type": "ComboPort", "value": "time"}, "decimals": {"customized": false, "type": "IntPort", "value": 6}, "every_n_ticks": {"customized": false, "type": "IntPort", "value": 1}, "fewer_buttons": {"customized": false, "type": "BoolPort", "value": false}, "font_size": {"customized": false, "type": "IntPort", "value": 10}, "ignore_signal_changes": {"customized": false, "type": "BoolPort", "value": false}, "initial_position": {"customized": false, "type": "ListPort", "value": [20, 20, 800, 800]}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "row_axis": {"customized": false, "type": "ComboPort", "value": "space"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_axes_table": {"customized": false, "type": "BoolPort", "value": true}, "show_data_table": {"customized": false, "type": "BoolPort", "value": true}, "show_markers_table": {"customized": false, "type": "BoolPort", "value": false}, "show_max_columns": {"customized": false, "type": "IntPort", "value": 20}, "show_max_values": {"customized": false, "type": "IntPort", "value": 50}, "show_streams_table": {"customized": false, "type": "BoolPort", "value": false}, "stream": {"customized": false, "type": "StringPort", "value": null}, "stream_name": {"customized": false, "type": "AliasPort", "value": null}, "verbose": {"customized": false, "type": "BoolPort", "value": true}, "window_title": {"customized": false, "type": "StringPort", "value": "Inspect Data Packet"}}, "uuid": "f3764eda-d7b3-41de-9547-e83f17880823"}}, "version": 1.1}</patch>
</scheme>
