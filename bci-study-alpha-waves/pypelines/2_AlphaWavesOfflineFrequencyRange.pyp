<?xml version='1.0' encoding='utf-8'?>
<scheme version="2.0" title="Occipital Study Alpha Waves Offline" description="">
	<nodes>
		<node id="0" name="Import XDF" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" project_name="NeuroPype" version="1.4.3" title="Import XDF" uuid="a33485d1-246c-4c3e-a497-0faebc6d7c5d" position="(-2100, 100)" />
		<node id="1" name="Dejitter Timestamps" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" project_name="NeuroPype" version="1.0.0" title="Dejitter Timestamps" uuid="e614371d-8f37-4883-abc2-2865b2b03e14" position="(-1900, 100)" />
		<node id="2" name="Set Axis Values" qualified_name="widgets.tensor_math.owsetaxisvalues.OWSetAxisValues" project_name="NeuroPype" version="0.2.0" title="Set Axis Values" uuid="3066e80b-e4a2-4a0e-b46a-802db98151b5" position="(-1800, 100)" />
		<node id="3" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Select Range" uuid="14c3affc-ba19-48e3-a7cd-90d99a5c3c59" position="(-1700, 100)" />
		<node id="4" name="Scrolling Plot (Offline)" qualified_name="widgets.visualization.owscrollplot.OWScrollPlot" project_name="NeuroPype" version="1.0.1" title="Scrolling Plot (Offline)" uuid="0f5ecea3-38bf-4dfd-9ef0-953af38c6ab0" position="(-1500, 0)" />
		<node id="5" name="Artifact Removal" qualified_name="widgets.neural.owartifactremoval.OWArtifactRemoval" project_name="NeuroPype" version="2.4.1" title="Artifact Removal" uuid="36862da6-5079-4e8f-a6dd-ab8793d51eec" position="(-1600, 100)" />
		<node id="6" name="Scrolling Plot (Offline)" qualified_name="widgets.visualization.owscrollplot.OWScrollPlot" project_name="NeuroPype" version="1.0.1" title="Scrolling Plot (Offline)" uuid="26be8eb5-44de-4f2e-b4fc-59594bdb58ab" position="(-1300, 0)" />
		<node id="7" name="Power Spectrum (Multitaper)" qualified_name="widgets.spectral.owmultitaperspectrum.OWMultitaperSpectrum" project_name="NeuroPype" version="1.2.1" title="Power Spectrum (Multitaper)" uuid="200f9db9-985c-40ea-9175-3d4d7070ab75" position="(-1400, 200)" />
		<node id="8" name="Segmentation" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" project_name="NeuroPype" version="1.0.2" title="Segmentation" uuid="964a5d8b-369d-44a2-bba8-88df027200a8" position="(-1600, 300)" />
		<node id="9" name="Frequency Normalization" qualified_name="widgets.signal_processing.owfrequencynormalization.OWFrequencyNormalization" project_name="NeuroPype" version="1.1.1" title="Frequency Normalization" uuid="f7abc1ea-3d13-49a8-a8ad-7d06832cd3e4" position="(-1300, 200)" />
		<node id="10" name="Insert Markers" qualified_name="widgets.markers.owinsertmarkers.OWInsertMarkers" project_name="NeuroPype" version="1.2.0" title="Insert Markers (EC)" uuid="41724c90-68be-4118-ac3c-eb5de598f395" position="(-1900, 300)" />
		<node id="11" name="Insert Markers" qualified_name="widgets.markers.owinsertmarkers.OWInsertMarkers" project_name="NeuroPype" version="1.2.0" title="Insert Markers (EO)" uuid="51d44fa2-52f6-4b8b-a681-0db811b684ea" position="(-1800, 300)" />
		<node id="12" name="Assign Target Values" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" project_name="NeuroPype" version="1.0.1" title="Assign Target Values" uuid="7ca2cdd3-1dfc-4d99-8942-81aa7edb8129" position="(-1700, 300)" />
		<node id="13" name="Strip Singleton Axis" qualified_name="widgets.tensor_math.owstripsingletonaxis.OWStripSingletonAxis" project_name="NeuroPype" version="1.0.0" title="Strip Singleton Axis" uuid="6f6303cf-2825-4c84-96ab-690ac0ef83c5" position="(-1200, 200)" />
		<node id="14" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Select Range" uuid="8b625aee-65a1-45c6-a4c7-ee4a5cf5d46f" position="(-1100, 200)" />
		<node id="15" name="Select Instances" qualified_name="widgets.formatting.owselectinstances.OWSelectInstances" project_name="NeuroPype" version="1.1.1" title="Select eyes-closed" uuid="7f6ff240-d5a7-4521-9bb2-aa81be8f4cbe" position="(-900, -100)" />
		<node id="16" name="Strip Singleton Axis" qualified_name="widgets.tensor_math.owstripsingletonaxis.OWStripSingletonAxis" project_name="NeuroPype" version="1.0.0" title="Strip Singleton Axis (Instance)" uuid="941e3f5e-011b-45d9-af47-a0f70a0ca95b" position="(-800, -100)" />
		<node id="17" name="Select Instances" qualified_name="widgets.formatting.owselectinstances.OWSelectInstances" project_name="NeuroPype" version="1.1.1" title="Select eyes-open" uuid="069ea29f-24eb-4778-8abe-d334c3a3eac4" position="(-900, 100)" />
		<node id="18" name="Strip Singleton Axis" qualified_name="widgets.tensor_math.owstripsingletonaxis.OWStripSingletonAxis" project_name="NeuroPype" version="1.0.0" title="Strip Singleton Axis (Instance)" uuid="e241d5b8-6213-4843-9d5c-825eeacf4ed6" position="(-800, 100)" />
		<node id="19" name="Grouped Mean" qualified_name="widgets.statistics.owgroupedmean.OWGroupedMean" project_name="NeuroPype" version="1.1.0" title="Grouped Mean" uuid="508a8777-950a-425f-9bff-314b32951853" position="(-1000, 0)" />
		<node id="20" name="Spectrum Plot" qualified_name="widgets.visualization.owspectrumplot.OWSpectrumPlot" project_name="NeuroPype" version="1.1.0" title="Spectrum Plot (Eyes Closed)" uuid="904ad073-554b-4cdf-8d9c-3607b17a8f4e" position="(-700, -100)" />
		<node id="21" name="Spectrum Plot" qualified_name="widgets.visualization.owspectrumplot.OWSpectrumPlot" project_name="NeuroPype" version="1.1.0" title="Spectrum Plot (Eyes Opened)" uuid="fb6e3321-ee43-4f82-9865-8b95fb90735c" position="(-700, 100)" />
		<node id="22" name="Peak Latency" qualified_name="widgets.signal_processing.owpeaklatency.OWPeakLatency" project_name="NeuroPype" version="1.0.0" title="Peak Latency" uuid="2990efc4-3df6-4251-8ca4-a252e1040f8c" position="(-900, 500)" />
		<node id="23" name="Select Instances" qualified_name="widgets.formatting.owselectinstances.OWSelectInstances" project_name="NeuroPype" version="1.1.1" title="Select eyes-closed" uuid="1883f714-3697-46d7-b6ff-2973b9e6ac1c" position="(-1000, 400)" />
		<node id="24" name="Streaming Bar Plot" qualified_name="widgets.visualization.owbarplot.OWBarPlot" project_name="NeuroPype" version="1.1.0" title="Bar Plot (alpha peak frequency)" uuid="3bab63c2-03f6-4e04-b065-b258333c19af" position="(-400, 600)" />
		<node id="25" name="Mean" qualified_name="widgets.statistics.owmean.OWMean" project_name="NeuroPype" version="1.0.0" title="Mean" uuid="de042a75-599e-45d6-9dcb-51d5435ca38e" position="(-500, 500)" />
		<node id="26" name="Streaming Bar Plot" qualified_name="widgets.visualization.owbarplot.OWBarPlot" project_name="NeuroPype" version="1.1.0" title="Bar Plot (alpha peak frequency)" uuid="7503b7ad-4e67-49c7-9e4d-2a3503fc5798" position="(-400, 400)" />
		<node id="27" name="Winsorize" qualified_name="widgets.statistics.owwinsorize.OWWinsorize" project_name="NeuroPype" version="0.8.0" title="Winsorize" uuid="cdf876c7-a595-4168-a5ce-3c516641d4ee" position="(-600, 500)" />
		<node id="28" name="Winsorize" qualified_name="widgets.statistics.owwinsorize.OWWinsorize" project_name="NeuroPype" version="0.8.0" title="Winsorize" uuid="3eb15d6f-aba8-42b4-9084-f428a97e5cce" position="(-600, 700)" />
		<node id="29" name="Mean" qualified_name="widgets.statistics.owmean.OWMean" project_name="NeuroPype" version="1.0.0" title="Mean" uuid="51ac9bd0-6479-4bfb-ae16-cb6d4d0ba531" position="(-500, 700)" />
		<node id="30" name="Streaming Bar Plot" qualified_name="widgets.visualization.owbarplot.OWBarPlot" project_name="NeuroPype" version="1.1.0" title="Bar Plot (alpha peak frequency)" uuid="6c103687-002f-471a-b290-b75fa0ef4df5" position="(-400, 200)" />
		<node id="31" name="Mean" qualified_name="widgets.statistics.owmean.OWMean" project_name="NeuroPype" version="1.0.0" title="Mean" uuid="7b1f66e4-fec0-4585-adef-260f70b0089b" position="(-500, 300)" />
		<node id="32" name="Winsorize" qualified_name="widgets.statistics.owwinsorize.OWWinsorize" project_name="NeuroPype" version="0.8.0" title="Winsorize" uuid="83fecc9e-4ee8-45c9-80fe-9f4ae26078db" position="(-600, 300)" />
		<node id="33" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.1.0" title="Select Range" uuid="66b1871a-9a7a-4de7-9aab-f7afea4e53ac" position="(-800, 500)" />
		<node id="34" name="Mean" qualified_name="widgets.statistics.owmean.OWMean" project_name="NeuroPype" version="1.0.0" title="Mean" uuid="d6f572c8-e00f-48a5-8322-a82b4486c0b4" position="(-200, 700)" />
		<node id="35" name="Winsorize" qualified_name="widgets.statistics.owwinsorize.OWWinsorize" project_name="NeuroPype" version="0.8.0" title="Winsorize" uuid="745d2bc5-7c74-4ccb-bdd8-810304315363" position="(-300, 700)" />
		<node id="36" name="Inspect Packet" qualified_name="widgets.visualization.owinspectpacket.OWInspectPacket" project_name="NeuroPype" version="3.0.1" title="Inspect Packet" uuid="4edb55e1-a9d2-4704-aaf2-10d4932902d2" position="(-100, 700)" />
		<node id="37" name="Mean" qualified_name="widgets.statistics.owmean.OWMean" project_name="NeuroPype" version="1.0.0" title="Mean" uuid="f66662b5-75a6-4929-881c-844e006ac52a" position="(-200, 300)" />
		<node id="38" name="Inspect Packet" qualified_name="widgets.visualization.owinspectpacket.OWInspectPacket" project_name="NeuroPype" version="3.0.1" title="Inspect Packet" uuid="3dd32fca-a3c7-4ec1-a33c-ae0dc88b731e" position="(-100, 300)" />
		<node id="39" name="Winsorize" qualified_name="widgets.statistics.owwinsorize.OWWinsorize" project_name="NeuroPype" version="0.8.0" title="Winsorize" uuid="4297dec0-9185-437b-bb92-9c13500aabea" position="(-300, 300)" />
		<node id="40" name="Parameter Port" qualified_name="widgets.workflow.owparameterport.OWParameterPort" project_name="NeuroPype" version="1.3.0" title="Parameter Port" uuid="df674904-43d5-4933-b210-878201c4049b" position="(-2300, 100)" />
	</nodes>
	<links>
		<link id="0" source_node_id="1" sink_node_id="2" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="1" source_node_id="2" sink_node_id="3" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="2" source_node_id="3" sink_node_id="4" source_channel="Data" sink_channel="Data" enabled="false" />
		<link id="3" source_node_id="3" sink_node_id="5" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="4" source_node_id="5" sink_node_id="6" source_channel="Data" sink_channel="Data" enabled="false" />
		<link id="5" source_node_id="8" sink_node_id="7" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="6" source_node_id="7" sink_node_id="9" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="7" source_node_id="10" sink_node_id="11" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="8" source_node_id="5" sink_node_id="10" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="9" source_node_id="11" sink_node_id="12" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="10" source_node_id="12" sink_node_id="8" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="11" source_node_id="9" sink_node_id="13" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="12" source_node_id="0" sink_node_id="1" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="13" source_node_id="13" sink_node_id="14" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="14" source_node_id="15" sink_node_id="16" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="15" source_node_id="17" sink_node_id="18" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="16" source_node_id="19" sink_node_id="15" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="17" source_node_id="19" sink_node_id="17" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="18" source_node_id="16" sink_node_id="20" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="19" source_node_id="18" sink_node_id="21" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="20" source_node_id="14" sink_node_id="19" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="21" source_node_id="25" sink_node_id="26" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="22" source_node_id="27" sink_node_id="25" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="23" source_node_id="28" sink_node_id="29" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="24" source_node_id="29" sink_node_id="24" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="25" source_node_id="31" sink_node_id="30" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="26" source_node_id="32" sink_node_id="31" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="27" source_node_id="14" sink_node_id="23" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="28" source_node_id="23" sink_node_id="22" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="29" source_node_id="22" sink_node_id="33" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="30" source_node_id="33" sink_node_id="32" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="31" source_node_id="33" sink_node_id="27" source_channel="Data" sink_channel="Data" enabled="false" />
		<link id="32" source_node_id="33" sink_node_id="28" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="33" source_node_id="29" sink_node_id="35" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="34" source_node_id="35" sink_node_id="34" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="35" source_node_id="34" sink_node_id="36" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="36" source_node_id="39" sink_node_id="37" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="37" source_node_id="37" sink_node_id="38" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="38" source_node_id="31" sink_node_id="39" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="39" source_node_id="40" sink_node_id="0" source_channel="Value" sink_channel="Filename" enabled="true" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties node_id="0" format="pickle">gASVdgIAAAAAAAB9lCiMDWNsb3VkX2FjY291bnSUjACUjAxjbG91ZF9idWNrZXSUaAKMEWNsb3Vk
X2NyZWRlbnRpYWxzlGgCjApjbG91ZF9ob3N0lIwHRGVmYXVsdJSMCGZpbGVuYW1llIyTRDovRGF0
YS9FeHBlcmltZW50UmVjb3JkZXIvU2ltcGxlQWxwaGFXYXZlc1N0dWR5L3JlY29yZGluZ3MvT0ND
SVBJVEFMX1NUVURZL01BTlRST1BPVi8yL01BTlRST1BPVl9hbHBoYV93YXZlc19jYWxpYnJhdGlv
bl8yMDIzLTA4LTExXzIxLTE1LTIwXzIueGRmlIwTaGFuZGxlX2Nsb2NrX3Jlc2V0c5SIjBFoYW5k
bGVfY2xvY2tfc3luY5SIjBVoYW5kbGVfaml0dGVyX3JlbW92YWyUiIwObWF4X21hcmtlcl9sZW6U
jA0odXNlIGRlZmF1bHQplIwIbWV0YWRhdGGUfZSMEnJlb3JkZXJfdGltZXN0YW1wc5SJjA5yZXRh
aW5fc3RyZWFtc5SMDSh1c2UgZGVmYXVsdCmUjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwO
X3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAA
BEsAAAHCAAAGNwAAA5gAAARMAAAB4QAABjYAAAOXAAAAAAAAAAAKAAAABEwAAAHhAAAGNgAAA5eU
hZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAt1c2VfY2FjaGluZ5SJjA91c2Vfc3RyZWFtbmFtZXOU
iYwHdmVyYm9zZZSJdS4=
</properties>
		<properties node_id="1" format="pickle">gASVCwEAAAAAAAB9lCiMD2ZvcmNlX21vbm90b25pY5SIjA9mb3JnZXRfaGFsZnRpbWWUS1qMDm1h
eF91cGRhdGVyYXRllE30AYwIbWV0YWRhdGGUfZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCU
jA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAA
AAADCwAAAX0AAAR0AAACdQAAAwwAAAGcAAAEcwAAAnQAAAAAAAAAAAeAAAADDAAAAZwAAARzAAAC
dJSFlIeUUpSMDnNldF9icmVha3BvaW50lImMDndhcm11cF9zYW1wbGVzlEr/////dS4=
</properties>
		<properties node_id="2" format="pickle">gASVqAEAAAAAAAB9lCiMCmFycmF5X25hbWWUjA0odXNlIGRlZmF1bHQplIwEYXhpc5SMBXNwYWNl
lIwKYXhpc19sYWJlbJSMDSh1c2UgZGVmYXVsdCmUjA9heGlzX29jY3VycmVuY2WUSwCMD2hhbmRs
ZV9leGlzdGluZ5SMC3JlcGxhY2UtYWxslIwIbWV0YWRhdGGUfZSMDG9ubHlfc2lnbmFsc5SIjBNz
YXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29y
ZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAABEsAAAINAAAFtAAAA00AAARMAAACLAAABbMAAANM
AAAAAAAAAAAKAAAABEwAAAIsAAAFswAAA0yUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAZ2YWx1
ZXOUXZQojANmcDGUjANmcDKUjANwbzOUjANwbzSUjAJwN5SMAnA4lIwCbzGUjAJvMpSMAmY3lIwC
ZjiUjAJmM5SMAmY0lIwCUHqUjAJPepSMAnAzlIwCcDSUZXUu
</properties>
		<properties node_id="3" format="pickle">gASVOAEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwFc3BhY2WUjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAARLAAACJgAABbQAAAMzAAAETAAAAkUAAAWzAAADMgAAAAAAAAAACgAA
AARMAAACRQAABbMAAAMylIWUh5RSlIwJc2VsZWN0aW9ulF2UKEsCSwNLBEsFSwZLB0sMSw1LDksP
ZYwOc2V0X2JyZWFrcG9pbnSUiYwEdW5pdJSMB2luZGljZXOUdS4=
</properties>
		<properties node_id="4" format="pickle">gASVQQIAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiYwLYW50aWFsaWFzZWSUiIwJYXV0b3NjYWxl
lImMEGJhY2tncm91bmRfY29sb3KUjAcjRkZGRkZGlIwQZGVjb3JhdGlvbl9jb2xvcpSMByMwMDAw
MDCUjAtkb3duc2FtcGxlZJSJjAxpbml0aWFsX2RpbXOUXZQoSzJLMk1YAk0gA2WMCmxpbmVfY29s
b3KUjAcjMDAwMDAwlIwKbGluZV93aWR0aJRHP+gAAAAAAACMDG1hcmtlcl9jb2xvcpSMByNGRjAw
MDCUjAhtZXRhZGF0YZR9lIwMbmFuc19hc196ZXJvlImMDm92ZXJyaWRlX3NyYXRllIwNKHVzZSBk
ZWZhdWx0KZSMDHBsb3RfbWFya2Vyc5SIjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3Vu
cGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAwsA
AADSAAAEdAAAAyAAAAMMAAAA8QAABHMAAAMfAAAAAAAAAAAHgAAAAwwAAADxAAAEcwAAAx+UhZSH
lFKUjAVzY2FsZZRHP7mZmZmZmZqMDnNldF9icmVha3BvaW50lImMC3N0cmVhbV9uYW1llGgUjAp0
aW1lX3JhbmdllEdAFAAAAAAAAIwFdGl0bGWUjAhSYXcgRGF0YZSMCnplcm9fY29sb3KUjAcjN0Y3
RjdGlIwIemVyb21lYW6UiHUu
</properties>
		<properties node_id="5" format="pickle">gASV/QIAAAAAAAB9lCiMAWGUjA0odXNlIGRlZmF1bHQplIwBYpSMDSh1c2UgZGVmYXVsdCmUjApi
bG9ja19zaXpllIwNKHVzZSBkZWZhdWx0KZSMDWNhbGliX3NlY29uZHOUSy2MBmN1dG9mZpRHQB4A
AAAAAACMD2VtaXRfY2FsaWJfZGF0YZSIjAdpbml0X29ulF2UjAlsb29rYWhlYWSUjA0odXNlIGRl
ZmF1bHQplIwQbWF4X2JhZF9jaGFubmVsc5RHP8mZmZmZmZqMCG1heF9kaW1zlEsAjBRtYXhfZHJv
cG91dF9mcmFjdGlvbpRHP7mZmZmZmZqMB21heF9tZW2UTQACjAhtZXRhZGF0YZR9lIwSbWluX2Ns
ZWFuX2ZyYWN0aW9ulEc/0AAAAAAAAIwVbWluX3JlcXVpcmVkX2NoYW5uZWxzlEsCjA1wcmVzZXJ2
ZV9iYW5klIwNKHVzZSBkZWZhdWx0KZSMCnJpZW1hbm5pYW6UiIwTc2F2ZWRXaWRnZXRHZW9tZXRy
eZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFycmF5lENC
AdnQywADAAAAAAMLAAAAgQAABHQAAANwAAADDAAAAKAAAARzAAADbwAAAAAAAAAAB4AAAAMMAAAA
oAAABHMAAANvlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwNc3RkZGV2X2N1dG9mZpRLD4wJc3Rl
cF9zaXpllEc/yZmZmZmZmowQdXNlX2NsZWFuX3dpbmRvd5SIjAp1c2VfbGVnYWN5lImMFndpbmRv
d19sZW5fY2xlYW53aW5kb3eURz/gAAAAAAAAjA13aW5kb3dfbGVuZ3RolEc/4AAAAAAAAIwOd2lu
ZG93X292ZXJsYXCURz/lHrhR64UfjBp3aW5kb3dfb3ZlcmxhcF9jbGVhbndpbmRvd5RHP+UeuFHr
hR+MEXpzY29yZV90aHJlc2hvbGRzlF2UKEr7////SwdldS4=
</properties>
		<properties node_id="6" format="pickle">gASVSgIAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiYwLYW50aWFsaWFzZWSUiIwJYXV0b3NjYWxl
lIiMEGJhY2tncm91bmRfY29sb3KUjAcjRkZGRkZGlIwQZGVjb3JhdGlvbl9jb2xvcpSMByMwMDAw
MDCUjAtkb3duc2FtcGxlZJSJjAxpbml0aWFsX2RpbXOUXZQoTbwCSzJNWAJNIANljApsaW5lX2Nv
bG9ylIwHIzAwMDAwMJSMCmxpbmVfd2lkdGiURz/oAAAAAAAAjAxtYXJrZXJfY29sb3KUjAcjRkYw
MDAwlIwIbWV0YWRhdGGUfZSMDG5hbnNfYXNfemVyb5SJjA5vdmVycmlkZV9zcmF0ZZSMDSh1c2Ug
ZGVmYXVsdCmUjAxwbG90X21hcmtlcnOUiIwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSMA3NpcJSMDl91
bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAAML
AAAA0gAABHQAAAMgAAADDAAAAPEAAARzAAADHwAAAAAAAAAAB4AAAAMMAAAA8QAABHMAAAMflIWU
h5RSlIwFc2NhbGWURz+5mZmZmZmajA5zZXRfYnJlYWtwb2ludJSJjAtzdHJlYW1fbmFtZZRoFIwK
dGltZV9yYW5nZZRHQBQAAAAAAACMBXRpdGxllIwQVGltZSBzZXJpZXMgdmlld5SMCnplcm9fY29s
b3KUjAcjN0Y3RjdGlIwIemVyb21lYW6UiHUu
</properties>
		<properties node_id="7" format="pickle">gASVIgEAAAAAAAB9lCiMGGF2ZXJhZ2Vfb3Zlcl90aW1lX3dpbmRvd5SJjA5oYWxmX2JhbmR3aWR0
aJRHQAQAAAAAAACMCG1ldGFkYXRhlH2UjARuZmZ0lIwNKHVzZSBkZWZhdWx0KZSMCm51bV90YXBl
cnOUaAaMCG9uZXNpZGVklIiME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVf
dHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAAETAAAAkUAAAWz
AAADMgAABEwAAAJFAAAFswAAAzIAAAAAAAAAAAoAAAAETAAAAkUAAAWzAAADMpSFlIeUUpSMDnNl
dF9icmVha3BvaW50lIl1Lg==
</properties>
		<properties node_id="8" format="pickle">gASVWAEAAAAAAAB9lCiMEWtlZXBfbWFya2VyX2NodW5rlImMDm1heF9nYXBfbGVuZ3RolEsAjAht
ZXRhZGF0YZR9lIwPb25saW5lX2Vwb2NoaW5nlIwNbWFya2VyLWxvY2tlZJSMDXNhbXBsZV9vZmZz
ZXSUSwCME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlR
dDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAAESwAAAg4AAAW0AAADSwAABEwAAAIt
AAAFswAAA0oAAAAAAAAAAAoAAAAETAAAAi0AAAWzAAADSpSFlIeUUpSMDnNlbGVjdF9tYXJrZXJz
lIwNKHVzZSBkZWZhdWx0KZSMDnNldF9icmVha3BvaW50lImMC3RpbWVfYm91bmRzlF2UKEsASwNl
jAd2ZXJib3NllIl1Lg==
</properties>
		<properties node_id="9" format="pickle">gASV8QAAAAAAAAB9lCiMBWFscGhhlEc/8AAAAAAAAIwTZml0X2ZyZXF1ZW5jeV9yYW5nZZSMDSh1
c2UgZGVmYXVsdCmUjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSMA3NpcJSMDl91
bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAARL
AAACRwAABbQAAAMSAAAETAAAAmYAAAWzAAADEQAAAAAAAAAACgAAAARMAAACZgAABbMAAAMRlIWU
h5RSlIwOc2V0X2JyZWFrcG9pbnSUiXUu
</properties>
		<properties node_id="10" format="pickle">gASVdwIAAAAAAAB9lCiMDWFuY2hvcl9tYXJrZXKUjBFjYWxpYnJhdGlvbi1jbG9zZZSMD2FuY2hv
cl9tYXJrZXJfQpSMEGNhbGlicmF0aW9uLW9wZW6UjAVjb3VudJRLAYwIY291bnRpbmeUjAlwZXJz
ZWNvbmSUjBdlbmZvcmNlX2ludGVybWl0dGVudF9pbpSMC21hcmtlci1zcGFulIwOZXhjZXB0X21h
cmtlcnOUXZSMDGV4dHJhX2xpbWl0c5RdlIwUaW5zdGFuY2VfZmllbGRzX2Zyb22UjAVmaXJzdJSM
FGludGVybWl0dGVudF9tYXJrZXJzlIwFYWxsb3eUjA1tYXJrZXJfZm9ybWF0lIwIdmVyYmF0aW2U
jAptYXhfbGVuZ3RolIwNKHVzZSBkZWZhdWx0KZSMCG1ldGFkYXRhlH2UjAptaW5fbGVuZ3RolIwN
KHVzZSBkZWZhdWx0KZSMBG1vZGWUjA5tYXJrZXItc3Bhbm5lZJSMB3BheWxvYWSUjAtleWVzLWNs
b3NlZJSMCXBsYWNlbWVudJSMC2VxdWlkaXN0YW50lIwLcmFuZG9tX3NlZWSUTTkwjBNzYXZlZFdp
ZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFC
eXRlQXJyYXmUQ0IB2dDLAAMAAAAAA+YAAAG1AAAFgAAAA8gAAAPmAAABtQAABYAAAAPIAAAAAAAA
AAAKAAAAA+YAAAG1AAAFgAAAA8iUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAt0aW1lX2xpbWl0
c5RdlChLAEr/////ZXUu
</properties>
		<properties node_id="11" format="pickle">gASVdQIAAAAAAAB9lCiMDWFuY2hvcl9tYXJrZXKUjBBjYWxpYnJhdGlvbi1vcGVulIwPYW5jaG9y
X21hcmtlcl9ClIwRY2FsaWJyYXRpb24tY2xvc2WUjAVjb3VudJRLAYwIY291bnRpbmeUjAlwZXJz
ZWNvbmSUjBdlbmZvcmNlX2ludGVybWl0dGVudF9pbpSMC21hcmtlci1zcGFulIwOZXhjZXB0X21h
cmtlcnOUXZSMDGV4dHJhX2xpbWl0c5RdlIwUaW5zdGFuY2VfZmllbGRzX2Zyb22UjAVmaXJzdJSM
FGludGVybWl0dGVudF9tYXJrZXJzlIwFYWxsb3eUjA1tYXJrZXJfZm9ybWF0lIwIdmVyYmF0aW2U
jAptYXhfbGVuZ3RolIwNKHVzZSBkZWZhdWx0KZSMCG1ldGFkYXRhlH2UjAptaW5fbGVuZ3RolIwN
KHVzZSBkZWZhdWx0KZSMBG1vZGWUjA5tYXJrZXItc3Bhbm5lZJSMB3BheWxvYWSUjAlleWVzLW9w
ZW6UjAlwbGFjZW1lbnSUjAtlcXVpZGlzdGFudJSMC3JhbmRvbV9zZWVklE05MIwTc2F2ZWRXaWRn
ZXRHZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0
ZUFycmF5lENCAdnQywADAAAAAAQzAAABsgAABc0AAAPFAAAEMwAAAbIAAAXNAAADxQAAAAAAAAAA
CgAAAAQzAAABsgAABc0AAAPFlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwLdGltZV9saW1pdHOU
XZQoSwBK/////2V1Lg==
</properties>
		<properties node_id="12" format="pickle">gASVaAEAAAAAAAB9lCiMEmFsc29fbGVnYWN5X291dHB1dJSJjA5pc19jYXRlZ29yaWNhbJSJjAlp
dl9jb2x1bW6UjAZNYXJrZXKUjAdtYXBwaW5nlF2UKIwLZXllcy1jbG9zZWSUjAlleWVzLW9wZW6U
ZYwObWFwcGluZ19mb3JtYXSUjAZjb21wYXSUjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRHZW9t
ZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFycmF5
lENCAdnQywADAAAAAARMAAACJgAABbMAAANSAAAETAAAAiYAAAWzAAADUgAAAAAAAAAACgAAAARM
AAACJgAABbMAAANSlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwRc3VwcG9ydF93aWxkY2FyZHOU
iYwLdXNlX251bWJlcnOUiYwHdmVyYm9zZZSJdS4=
</properties>
		<properties node_id="13" format="pickle">gASVyAAAAAAAAAB9lCiMBGF4aXOUjAR0aW1llIwIbWV0YWRhdGGUfZSME3NhdmVkV2lkZ2V0R2Vv
bWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJh
eZRDQgHZ0MsAAwAAAAAESgAAAjQAAAWzAAAC5wAABEsAAAJTAAAFsgAAAuYAAAAAAAAAAAoAAAAE
SwAAAlMAAAWyAAAC5pSFlIeUUpSMDnNldF9icmVha3BvaW50lIl1Lg==
</properties>
		<properties node_id="14" format="pickle">gASVKgEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwJZnJlcXVlbmN5lIwIbWV0YWRhdGGUfZSME3NhdmVkV2lk
Z2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5
dGVBcnJheZRDQgHZ0MsAAwAAAAAESwAAAiYAAAW0AAADMwAABEwAAAJFAAAFswAAAzIAAAAAAAAA
AAoAAAAETAAAAkUAAAWzAAADMpSFlIeUUpSMCXNlbGVjdGlvbpSMCDAuNS4uLjYwlIwOc2V0X2Jy
ZWFrcG9pbnSUiYwEdW5pdJSMAkh6lHUu
</properties>
		<properties node_id="15" format="pickle">gASVngEAAAAAAAB9lCiME2Fzc2lnbl90YXJnZXRfdmFsdWWUjA0odXNlIGRlZmF1bHQplIwQY29t
YmluZV9wcmV2aW91c5SMCG92ZXJyaWRllIwSY29tYmluZV9zZWxlY3Rpb25zlIwDYW5klIwJY29u
ZGl0aW9ulIwAlIwbZGVmYXVsdF9jb21wYXJpc29uX29wZXJhdG9ylIwEYXV0b5SMEGRyb3BfaW1t
ZWRpYXRlbHmUiIwQaW52ZXJ0X3NlbGVjdGlvbpSJjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAARLAAACAgAABbQAAANXAAAETAAAAiEAAAWzAAADVgAAAAAAAAAACgAA
AARMAAACIQAABbMAAANWlIWUh5RSlIwJc2VsZWN0aW9ulH2UjAZNYXJrZXKUXZSMC2V5ZXMtY2xv
c2VklGFzjA5zZXRfYnJlYWtwb2ludJSJdS4=
</properties>
		<properties node_id="16" format="pickle">gASVzAAAAAAAAAB9lCiMBGF4aXOUjAhpbnN0YW5jZZSMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdl
dEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRl
QXJyYXmUQ0IB2dDLAAMAAAAABEsAAAJTAAAFtAAAAwYAAARMAAACcgAABbMAAAMFAAAAAAAAAAAK
AAAABEwAAAJyAAAFswAAAwWUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJdS4=
</properties>
		<properties node_id="17" format="pickle">gASVnAEAAAAAAAB9lCiME2Fzc2lnbl90YXJnZXRfdmFsdWWUjA0odXNlIGRlZmF1bHQplIwQY29t
YmluZV9wcmV2aW91c5SMCG92ZXJyaWRllIwSY29tYmluZV9zZWxlY3Rpb25zlIwDYW5klIwJY29u
ZGl0aW9ulIwAlIwbZGVmYXVsdF9jb21wYXJpc29uX29wZXJhdG9ylIwEYXV0b5SMEGRyb3BfaW1t
ZWRpYXRlbHmUiIwQaW52ZXJ0X3NlbGVjdGlvbpSJjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAARLAAACAgAABbQAAANXAAAETAAAAiEAAAWzAAADVgAAAAAAAAAACgAA
AARMAAACIQAABbMAAANWlIWUh5RSlIwJc2VsZWN0aW9ulH2UjAZNYXJrZXKUXZSMCWV5ZXMtb3Bl
bpRhc4wOc2V0X2JyZWFrcG9pbnSUiXUu
</properties>
		<properties node_id="18" format="pickle">gASVzAAAAAAAAAB9lCiMBGF4aXOUjAhpbnN0YW5jZZSMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdl
dEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRl
QXJyYXmUQ0IB2dDLAAMAAAAABEsAAAJTAAAFtAAAAwYAAARMAAACcgAABbMAAAMFAAAAAAAAAAAK
AAAABEwAAAJyAAAFswAAAwWUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJdS4=
</properties>
		<properties node_id="19" format="pickle">gASVkQEAAAAAAAB9lCiMDWFsbG93X21hcmtlcnOUiIwIY2lfcmFuZ2WURz/uZmZmZmZmjARkZG9m
lEsBjAllcXVhbF92YXKUiYwKZXJyb3JfdHlwZZSMBG5vbmWUjAlmaWxsX2NvbHOUiIwKZ3JvdXBf
Y29sc5RdlIwGTWFya2VylGGMDWdyb3VwaW5nX3R5cGWUjAZsZXZlbHOUjAltZWFuX3R5cGWUjARt
ZWFulIwIbWV0YWRhdGGUfZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVf
dHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAAESwAAAdcAAAW0
AAADgwAABEwAAAH2AAAFswAAA4IAAAAAAAAAAAoAAAAETAAAAfYAAAWzAAADgpSFlIeUUpSMDnNl
dF9icmVha3BvaW50lImMD3RyaW1fcHJvcG9ydGlvbpRdlChLAEsAZYwLdXNlX2NhY2hpbmeUiYwJ
d2luc29yaXpllIl1Lg==
</properties>
		<properties node_id="20" format="pickle">gASVIQIAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiYwLYW50aWFsaWFzZWSUiIwQYXV0b19saW5l
X2NvbG9yc5SJjAlhdXRvc2NhbGWUiYwQYmFja2dyb3VuZF9jb2xvcpSMByNGRkZGRkaUjBBkZWNv
cmF0aW9uX2NvbG9ylIwHIzAwMDAwMJSMC2Rvd25zYW1wbGVklImMDGluaXRpYWxfZGltc5RdlChN
bAJLCk1YAk30AWWMCmxpbmVfY29sb3KUjAcjMDAwMDAwlIwKbGluZV93aWR0aJRHP+gAAAAAAACM
CG1ldGFkYXRhlH2UjBVvbmVfb3Zlcl9mX2NvcnJlY3Rpb26UiYwTc2F2ZWRXaWRnZXRHZW9tZXRy
eZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFycmF5lENC
AdnQywADAAAAAARLAAABqgAABswAAAOwAAAETAAAAckAAAbLAAADrwAAAAAAAAAACgAAAARMAAAB
yQAABssAAAOvlIWUh5RSlIwFc2NhbGWURz+EeuFHrhR7jA5zZXRfYnJlYWtwb2ludJSJjAdzdGFj
a2VklImMC3N0cmVhbV9uYW1llIwNKHVzZSBkZWZhdWx0KZSMBXRpdGxllIwbU3BlY3RydW0gUGxv
dCAoRXllcyBDbG9zZWQplIwKemVyb19jb2xvcpSMCSM3RjdGN0Y3RpR1Lg==
</properties>
		<properties node_id="21" format="pickle">gASVIAIAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiYwLYW50aWFsaWFzZWSUiIwQYXV0b19saW5l
X2NvbG9yc5SJjAlhdXRvc2NhbGWUiYwQYmFja2dyb3VuZF9jb2xvcpSMByNGRkZGRkaUjBBkZWNv
cmF0aW9uX2NvbG9ylIwHIzAwMDAwMJSMC2Rvd25zYW1wbGVklImMDGluaXRpYWxfZGltc5RdlChL
CksKTVgCTfQBZYwKbGluZV9jb2xvcpSMByMwMDAwMDCUjApsaW5lX3dpZHRolEc/6AAAAAAAAIwI
bWV0YWRhdGGUfZSMFW9uZV9vdmVyX2ZfY29ycmVjdGlvbpSJjBNzYXZlZFdpZGdldEdlb21ldHJ5
lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB
2dDLAAMAAAAABEsAAAGqAAAGzAAAA7AAAARMAAAByQAABssAAAOvAAAAAAAAAAAKAAAABEwAAAHJ
AAAGywAAA6+UhZSHlFKUjAVzY2FsZZRHP4R64UeuFHuMDnNldF9icmVha3BvaW50lImMB3N0YWNr
ZWSUiYwLc3RyZWFtX25hbWWUjA0odXNlIGRlZmF1bHQplIwFdGl0bGWUjBtTcGVjdHJ1bSBQbG90
IChFeWVzIE9wZW5lZCmUjAp6ZXJvX2NvbG9ylIwJIzdGN0Y3RjdGlHUu
</properties>
		<properties node_id="22" format="pickle">gASVLgEAAAAAAAB9lCiMFWFjY291bnRfZm9yX3RpbWVfYXhpc5SJjARheGlzlIwJZnJlcXVlbmN5
lIwIbWV0YWRhdGGUfZSMCG5lZ2F0aXZllImME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5f
dW5waWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAAD
CwAAAWkAAAR0AAACiAAAAwwAAAGIAAAEcwAAAocAAAAAAAAAAAoAAAADDAAAAYgAAARzAAACh5SF
lIeUUpSMDnNldF9icmVha3BvaW50lImMFXN1YnRyYWN0X2ZpbHRlcl9kZWxheZSJjAR1bml0lIwC
SHqUjBN1cGRhdGVfb25fc3RyZWFtaW5nlIh1Lg==
</properties>
		<properties node_id="23" format="pickle">gASVngEAAAAAAAB9lCiME2Fzc2lnbl90YXJnZXRfdmFsdWWUjA0odXNlIGRlZmF1bHQplIwQY29t
YmluZV9wcmV2aW91c5SMCG92ZXJyaWRllIwSY29tYmluZV9zZWxlY3Rpb25zlIwDYW5klIwJY29u
ZGl0aW9ulIwAlIwbZGVmYXVsdF9jb21wYXJpc29uX29wZXJhdG9ylIwEYXV0b5SMEGRyb3BfaW1t
ZWRpYXRlbHmUiIwQaW52ZXJ0X3NlbGVjdGlvbpSJjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAAMLAAABTgAABHQAAAKjAAADDAAAAW0AAARzAAACogAAAAAAAAAACgAA
AAMMAAABbQAABHMAAAKilIWUh5RSlIwJc2VsZWN0aW9ulH2UjAZNYXJrZXKUXZSMC2V5ZXMtY2xv
c2VklGFzjA5zZXRfYnJlYWtwb2ludJSJdS4=
</properties>
		<properties node_id="24" format="pickle">gASVRAIAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiYwPYXV0b19iYXJfY29sb3JzlImMBGF4aXOU
jAVzcGFjZZSMEGJhY2tncm91bmRfY29sb3KUjAcjRkZGRkZGlIwJYmFyX2NvbG9ylIwBYpSMCWJh
cl93aWR0aJRHP9UeuFHrhR+MCGNvbG9ybWFwlIwFdHVyYm+UjAlmb250X3NpemWUR0AkAAAAAAAA
jAxpbml0aWFsX2RpbXOUXZQoSwpNHAJNWAJNkAFljA5pbnN0YW5jZV9maWVsZJSMDSh1c2UgZGVm
YXVsdCmUjA5sYWJlbF9yb3RhdGlvbpSMCmhvcml6b250YWyUjAtsZWZ0X29mZnNldJRLAIwIbWV0
YWRhdGGUfZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwM
UHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAA///7OAAAAm3///yfAAAEdP//+zgA
AAJt///8nwAABHQAAAABAAAAAAeA///7OAAAAm3///yfAAAEdJSFlIeUUpSMDnNldF9icmVha3Bv
aW50lImMDHNob3dfdG9vbGJhcpSJjAtzdHJlYW1fbmFtZZSMDSh1c2UgZGVmYXVsdCmUjAV0aXRs
ZZSMKUFscGhhIFBlYWsgRnJlcXVlbmN5IHwgRUMgLSBMb3cgTWVhbiAoSHoplIwHdmVyYm9zZZSJ
jAh5X2xpbWl0c5RdlChLBUsoZXUu
</properties>
		<properties node_id="25" format="pickle">gASVXAEAAAAAAAB9lCiMBGF4aXOUjAhpbnN0YW5jZZSMD2NvbXB1dGVfYmFja2VuZJSMBGtlZXCU
jBJmb3JjZV9mZWF0dXJlX2F4aXOUiYwLaWdub3JlX25hbnOUiYwIbWV0YWRhdGGUfZSMCXByZWNp
c2lvbpSMBGtlZXCUjAZyb2J1c3SUiYwVcm9idXN0X2VzdGltYXRvcl90eXBllIwGbWVkaWFulIwT
c2F2ZWRXaWRnZXRHZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENv
cmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAAQEAAACAwAABW0AAANwAAAEBQAAAiIAAAVsAAAD
bwAAAAAAAAAACgAAAAQFAAACIgAABWwAAANvlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwPdHJp
bV9wcm9wb3J0aW9ulEsAdS4=
</properties>
		<properties node_id="26" format="pickle">gASVQAIAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiYwPYXV0b19iYXJfY29sb3JzlImMBGF4aXOU
jAVzcGFjZZSMEGJhY2tncm91bmRfY29sb3KUjAcjRkZGRkZGlIwJYmFyX2NvbG9ylIwBYpSMCWJh
cl93aWR0aJRHP9UeuFHrhR+MCGNvbG9ybWFwlIwFdHVyYm+UjAlmb250X3NpemWUR0AkAAAAAAAA
jAxpbml0aWFsX2RpbXOUXZQoTX4ES8hNvAJN9AFljA5pbnN0YW5jZV9maWVsZJSMDSh1c2UgZGVm
YXVsdCmUjA5sYWJlbF9yb3RhdGlvbpSMCmhvcml6b250YWyUjAtsZWZ0X29mZnNldJRLAIwIbWV0
YWRhdGGUfZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwM
UHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAA///7tQAAAlT///1EAAAEe///+7YA
AAJz///9QwAABHoAAAABAAAAAAeA///7tgAAAnP///1DAAAEepSFlIeUUpSMDnNldF9icmVha3Bv
aW50lImMDHNob3dfdG9vbGJhcpSJjAtzdHJlYW1fbmFtZZSMDSh1c2UgZGVmYXVsdCmUjAV0aXRs
ZZSMJUFscGhhIFBlYWsgRnJlcXVlbmN5IHwgRUMgLSBNZWFuIChIeimUjAd2ZXJib3NllImMCHlf
bGltaXRzlF2UKEsFSyhldS4=
</properties>
		<properties node_id="27" format="pickle">gASVCAEAAAAAAAB9lCiMBGF4aXOUjAhpbnN0YW5jZZSMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdl
dEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRl
QXJyYXmUQ0IB2dDLAAMAAAAABCcAAAJUAAAFjgAAAxcAAAQnAAACVAAABY4AAAMXAAAAAAAAAAAK
AAAABCcAAAJUAAAFjgAAAxeUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjA90cmltX3Byb3BvcnRp
b26URz/TMzMzMzMzjBV0cmltX3Byb3BvcnRpb25fbG93ZXKURz/TMzMzMzMzdS4=
</properties>
		<properties node_id="28" format="pickle">gASVAQEAAAAAAAB9lCiMBGF4aXOUjAhpbnN0YW5jZZSMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdl
dEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRl
QXJyYXmUQ0IB2dDLAAMAAAAABEsAAAI7AAAFtAAAAx4AAARMAAACWgAABbMAAAMdAAAAAAAAAAAK
AAAABEwAAAJaAAAFswAAAx2UhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjA90cmltX3Byb3BvcnRp
b26URz/mZmZmZmZmjBV0cmltX3Byb3BvcnRpb25fbG93ZXKUSwB1Lg==
</properties>
		<properties node_id="29" format="pickle">gASVXAEAAAAAAAB9lCiMBGF4aXOUjAhpbnN0YW5jZZSMD2NvbXB1dGVfYmFja2VuZJSMBGtlZXCU
jBJmb3JjZV9mZWF0dXJlX2F4aXOUiYwLaWdub3JlX25hbnOUiYwIbWV0YWRhdGGUfZSMCXByZWNp
c2lvbpSMBGtlZXCUjAZyb2J1c3SUiYwVcm9idXN0X2VzdGltYXRvcl90eXBllIwGbWVkaWFulIwT
c2F2ZWRXaWRnZXRHZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENv
cmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAARLAAACBAAABbQAAANWAAAETAAAAiMAAAWzAAAD
VQAAAAAAAAAACgAAAARMAAACIwAABbMAAANVlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwPdHJp
bV9wcm9wb3J0aW9ulEsAdS4=
</properties>
		<properties node_id="30" format="pickle">gASVRgIAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiYwPYXV0b19iYXJfY29sb3JzlImMBGF4aXOU
jAVzcGFjZZSMEGJhY2tncm91bmRfY29sb3KUjAcjRkZGRkZGlIwJYmFyX2NvbG9ylIwBYpSMCWJh
cl93aWR0aJRHP9UeuFHrhR+MCGNvbG9ybWFwlIwFdHVyYm+UjAlmb250X3NpemWUR0AkAAAAAAAA
jAxpbml0aWFsX2RpbXOUXZQoTWwCTRwCTVgCTZABZYwOaW5zdGFuY2VfZmllbGSUjA0odXNlIGRl
ZmF1bHQplIwObGFiZWxfcm90YXRpb26UjApob3Jpem9udGFslIwLbGVmdF9vZmZzZXSUSwCMCG1l
dGFkYXRhlH2UjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SM
DFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAP//+r4AAAI1///8JwAABFz///q/
AAACVP///CYAAARbAAAAAQAAAAAHgP//+r8AAAJU///8JgAABFuUhZSHlFKUjA5zZXRfYnJlYWtw
b2ludJSJjAxzaG93X3Rvb2xiYXKUiYwLc3RyZWFtX25hbWWUjA0odXNlIGRlZmF1bHQplIwFdGl0
bGWUjCpBbHBoYSBQZWFrIEZyZXF1ZW5jeSB8IEVDIC0gSGlnaCBNZWFuIChIeimUjAd2ZXJib3Nl
lImMCHlfbGltaXRzlF2UKEsFSyhldS4=
</properties>
		<properties node_id="31" format="pickle">gASVXAEAAAAAAAB9lCiMBGF4aXOUjAhpbnN0YW5jZZSMD2NvbXB1dGVfYmFja2VuZJSMBGtlZXCU
jBJmb3JjZV9mZWF0dXJlX2F4aXOUiYwLaWdub3JlX25hbnOUiYwIbWV0YWRhdGGUfZSMCXByZWNp
c2lvbpSMBGtlZXCUjAZyb2J1c3SUiYwVcm9idXN0X2VzdGltYXRvcl90eXBllIwGbWVkaWFulIwT
c2F2ZWRXaWRnZXRHZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENv
cmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAARLAAACBAAABbQAAANWAAAETAAAAiMAAAWzAAAD
VQAAAAAAAAAACgAAAARMAAACIwAABbMAAANVlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwPdHJp
bV9wcm9wb3J0aW9ulEsAdS4=
</properties>
		<properties node_id="32" format="pickle">gASVCAEAAAAAAAB9lCiMBGF4aXOUjAhpbnN0YW5jZZSMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdl
dEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRl
QXJyYXmUQ0IB2dDLAAMAAAAABEsAAAI7AAAFtAAAAx4AAARMAAACWgAABbMAAAMdAAAAAAAAAAAK
AAAABEwAAAJaAAAFswAAAx2UhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjA90cmltX3Byb3BvcnRp
b26URz+5mZmZmZmajBV0cmltX3Byb3BvcnRpb25fbG93ZXKURz/mZmZmZmZmdS4=
</properties>
		<properties node_id="33" format="pickle">gASVIgEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwFc3BhY2WUjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAD///uLAAAC2v///PQAAAQC///7jAAAAvn///zzAAAEAQAAAAEAAAAAB4D/
//uMAAAC+f///PMAAAQBlIWUh5RSlIwJc2VsZWN0aW9ulIwBOpSMDnNldF9icmVha3BvaW50lImM
BHVuaXSUjAVuYW1lc5R1Lg==
</properties>
		<properties node_id="34" format="pickle">gASVYAEAAAAAAAB9lCiMBGF4aXOUjAVzcGFjZZSMD2NvbXB1dGVfYmFja2VuZJSMBGtlZXCUjBJm
b3JjZV9mZWF0dXJlX2F4aXOUiYwLaWdub3JlX25hbnOUiYwIbWV0YWRhdGGUfZSMCXByZWNpc2lv
bpSMBGtlZXCUjAZyb2J1c3SUiYwVcm9idXN0X2VzdGltYXRvcl90eXBllIwGbWVkaWFulIwTc2F2
ZWRXaWRnZXRHZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWU
jApRQnl0ZUFycmF5lENCAdnQywADAAD///uLAAACuP///PQAAAQK///7jAAAAtf///zzAAAECQAA
AAEAAAAAB4D///uMAAAC1////PMAAAQJlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwPdHJpbV9w
cm9wb3J0aW9ulEc/yZmZmZmZmnUu
</properties>
		<properties node_id="35" format="pickle">gASVBQEAAAAAAAB9lCiMBGF4aXOUjAVzcGFjZZSMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdl
b21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJy
YXmUQ0IB2dDLAAMAAP//+4sAAALv///89AAAA9L///uMAAADDv///PMAAAPRAAAAAQAAAAAHgP//
+4wAAAMO///88wAAA9GUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjA90cmltX3Byb3BvcnRpb26U
Rz/JmZmZmZmajBV0cmltX3Byb3BvcnRpb25fbG93ZXKURz/JmZmZmZmadS4=
</properties>
		<properties node_id="36" format="pickle">gASVGwIAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiIwIY29sX2F4aXOUjARub25llIwIZGVjaW1h
bHOUSwaMDWV2ZXJ5X25fdGlja3OUSwGMDWZld2VyX2J1dHRvbnOUiYwJZm9udF9zaXpllEsKjBBp
bml0aWFsX3Bvc2l0aW9ulF2UKE3iBE0sAU0sAUtkZYwIbWV0YWRhdGGUfZSMCHJvd19heGlzlIwF
c3BhY2WUjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5
UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAP//+4sAAAJS///89AAABHD///uMAAAC
cf///PMAAARvAAAAAQAAAAAHgP//+4wAAAJx///88wAABG+UhZSHlFKUjA5zZXRfYnJlYWtwb2lu
dJSJjA9zaG93X2F4ZXNfdGFibGWUiIwPc2hvd19kYXRhX3RhYmxllIiMEnNob3dfbWFya2Vyc190
YWJsZZSJjBBzaG93X21heF9jb2x1bW5zlEsUjA9zaG93X21heF92YWx1ZXOUSzKMEnNob3dfc3Ry
ZWFtc190YWJsZZSJjAtzdHJlYW1fbmFtZZSMDSh1c2UgZGVmYXVsdCmUjAd2ZXJib3NllIiMDHdp
bmRvd190aXRsZZSMFVN1Z2dlc3RlZCBMb3dlciBMaW1pdJR1Lg==
</properties>
		<properties node_id="37" format="pickle">gASVYAEAAAAAAAB9lCiMBGF4aXOUjAVzcGFjZZSMD2NvbXB1dGVfYmFja2VuZJSMBGtlZXCUjBJm
b3JjZV9mZWF0dXJlX2F4aXOUiYwLaWdub3JlX25hbnOUiYwIbWV0YWRhdGGUfZSMCXByZWNpc2lv
bpSMBGtlZXCUjAZyb2J1c3SUiYwVcm9idXN0X2VzdGltYXRvcl90eXBllIwGbWVkaWFulIwTc2F2
ZWRXaWRnZXRHZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWU
jApRQnl0ZUFycmF5lENCAdnQywADAAD///uLAAACuP///PQAAAQK///7jAAAAtf///zzAAAECQAA
AAEAAAAAB4D///uMAAAC1////PMAAAQJlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwPdHJpbV9w
cm9wb3J0aW9ulEc/yZmZmZmZmnUu
</properties>
		<properties node_id="38" format="pickle">gASVGwIAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiIwIY29sX2F4aXOUjARub25llIwIZGVjaW1h
bHOUSwaMDWV2ZXJ5X25fdGlja3OUSwGMDWZld2VyX2J1dHRvbnOUiYwJZm9udF9zaXpllEsKjBBp
bml0aWFsX3Bvc2l0aW9ulF2UKE3iBE30AU0sAUtkZYwIbWV0YWRhdGGUfZSMCHJvd19heGlzlIwF
c3BhY2WUjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5
UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAP//+4sAAAJS///89AAABHD///uMAAAC
cf///PMAAARvAAAAAQAAAAAHgP//+4wAAAJx///88wAABG+UhZSHlFKUjA5zZXRfYnJlYWtwb2lu
dJSJjA9zaG93X2F4ZXNfdGFibGWUiIwPc2hvd19kYXRhX3RhYmxllIiMEnNob3dfbWFya2Vyc190
YWJsZZSJjBBzaG93X21heF9jb2x1bW5zlEsUjA9zaG93X21heF92YWx1ZXOUSzKMEnNob3dfc3Ry
ZWFtc190YWJsZZSJjAtzdHJlYW1fbmFtZZSMDSh1c2UgZGVmYXVsdCmUjAd2ZXJib3NllIiMDHdp
bmRvd190aXRsZZSMFVN1Z2dlc3RlZCBVcHBlciBMaW1pdJR1Lg==
</properties>
		<properties node_id="39" format="pickle">gASVBQEAAAAAAAB9lCiMBGF4aXOUjAVzcGFjZZSMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdl
b21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJy
YXmUQ0IB2dDLAAMAAP//+4sAAALv///89AAAA9L///uMAAADDv///PMAAAPRAAAAAQAAAAAHgP//
+4wAAAMO///88wAAA9GUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjA90cmltX3Byb3BvcnRpb26U
Rz/JmZmZmZmajBV0cmltX3Byb3BvcnRpb25fbG93ZXKURz/JmZmZmZmadS4=
</properties>
		<properties node_id="40" format="pickle">gASVJgIAAAAAAAB9lCiMCGF1dG9jYXN0lIiMCWNhbmJlbm9uZZSIjAdkZWZhdWx0lIxVQzpcYmNp
LWNvbnRyb2xcYmNpLXN0dWR5LWFscGhhLXdhdmVzXGV4YW1wbGVfZGF0YVxhbHBoYV93YXZlc19j
YWxpYnJhdGlvbl9leGFtcGxlLnhkZpSMBGRlc2OUjACUjAZkb21haW6UjA0odXNlIGRlZmF1bHQp
lIwIZWRpdGFibGWUiIwGZXhwZXJ0lImMC2lzX2ZpbGVuYW1llImMCmlzX3Zpc2libGWUiIwIbWV0
YWRhdGGUfZSMDXBvcnRfY2F0ZWdvcnmUaAaMCHBvcnRuYW1llIwIRmlsZW5hbWWUjA1yZWxhdGlv
bnNoaXBzlF2UjARzYWZllImME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVf
dHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAA///7iwAAAkn///z0
AAAEef//+4wAAAJo///88wAABHgAAAABAAAAAAeA///7jAAAAmj///zzAAAEeJSFlIeUUpSMBnNl
bGVjdJSMBG5vbmWUjBNzZW5kX3NpZ25hbF9jaGFuZ2VklIiMDnNldF9icmVha3BvaW50lImMCnZh
bHVlX3R5cGWUjAZzdHJpbmeUjAd2ZXJib3NllImMDHZlcmJvc2VfbmFtZZRoCHUu
</properties>
	</node_properties>
	<patch>{"description": {"description": "", "license": "", "name": "Occipital Study Alpha Waves Offline", "status": "(unspecified)", "url": "", "version": "0.0.0"}, "edges": [["node2", "data", "node3", "data"], ["node3", "data", "node4", "data"], ["node4", "data", "node6", "data"], ["node9", "data", "node8", "data"], ["node8", "data", "node10", "data"], ["node11", "data", "node12", "data"], ["node6", "data", "node11", "data"], ["node12", "data", "node13", "data"], ["node13", "data", "node9", "data"], ["node10", "data", "node14", "data"], ["node1", "data", "node2", "data"], ["node14", "data", "node15", "data"], ["node16", "data", "node17", "data"], ["node18", "data", "node19", "data"], ["node20", "data", "node16", "data"], ["node20", "data", "node18", "data"], ["node17", "data", "node21", "data"], ["node19", "data", "node22", "data"], ["node15", "data", "node20", "data"], ["node15", "data", "node24", "data"], ["node26", "data", "node27", "data"], ["node28", "data", "node26", "data"], ["node29", "data", "node30", "data"], ["node30", "data", "node25", "data"], ["node30", "data", "node36", "data"], ["node32", "data", "node31", "data"], ["node32", "data", "node40", "data"], ["node33", "data", "node32", "data"], ["node24", "data", "node23", "data"], ["node23", "data", "node34", "data"], ["node34", "data", "node33", "data"], ["node34", "data", "node29", "data"], ["node36", "data", "node35", "data"], ["node35", "data", "node37", "data"], ["node40", "data", "node38", "data"], ["node38", "data", "node39", "data"], ["node41", "value", "node1", "filename"]], "nodes": {"node1": {"class": "ImportXDF", "module": "neuropype.nodes.file_system.ImportXDF", "params": {"cloud_account": {"customized": false, "type": "StringPort", "value": ""}, "cloud_bucket": {"customized": false, "type": "StringPort", "value": ""}, "cloud_credentials": {"customized": false, "type": "StringPort", "value": ""}, "cloud_host": {"customized": false, "type": "EnumPort", "value": "Default"}, "filename": {"customized": true, "type": "StringPort", "value": "C:/bci-control/bci-study-alpha-waves/example_data/alpha_waves_calibration_example.xdf"}, "handle_clock_resets": {"customized": false, "type": "BoolPort", "value": true}, "handle_clock_sync": {"customized": false, "type": "BoolPort", "value": true}, "handle_jitter_removal": {"customized": false, "type": "BoolPort", "value": true}, "max_marker_len": {"customized": false, "type": "IntPort", "value": null}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "reorder_timestamps": {"customized": false, "type": "BoolPort", "value": false}, "retain_streams": {"customized": false, "type": "Port", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "use_caching": {"customized": false, "type": "BoolPort", "value": false}, "use_streamnames": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "a33485d1-246c-4c3e-a497-0faebc6d7c5d"}, "node10": {"class": "FrequencyNormalization", "module": "neuropype.nodes.signal_processing.FrequencyNormalization", "params": {"alpha": {"customized": false, "type": "FloatPort", "value": 1.0}, "fit_frequency_range": {"customized": false, "type": "ListPort", "value": null}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "f7abc1ea-3d13-49a8-a8ad-7d06832cd3e4"}, "node11": {"class": "InsertMarkers", "module": "neuropype.nodes.markers.InsertMarkers", "params": {"anchor_marker": {"customized": true, "type": "Port", "value": "calibration-close"}, "anchor_marker_B": {"customized": true, "type": "Port", "value": "calibration-open"}, "count": {"customized": false, "type": "FloatPort", "value": 1}, "counting": {"customized": true, "type": "EnumPort", "value": "persecond"}, "enforce_intermittent_in": {"customized": false, "type": "EnumPort", "value": "marker-span"}, "except_markers": {"customized": false, "type": "ListPort", "value": []}, "extra_limits": {"customized": false, "type": "ListPort", "value": []}, "instance_fields_from": {"customized": false, "type": "EnumPort", "value": "first"}, "intermittent_markers": {"customized": false, "type": "EnumPort", "value": "allow"}, "marker_format": {"customized": false, "type": "EnumPort", "value": "verbatim"}, "max_length": {"customized": false, "type": "FloatPort", "value": null}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "min_length": {"customized": false, "type": "FloatPort", "value": null}, "mode": {"customized": true, "type": "EnumPort", "value": "marker-spanned"}, "payload": {"customized": true, "type": "Port", "value": "eyes-closed"}, "placement": {"customized": false, "type": "EnumPort", "value": "equidistant"}, "random_seed": {"customized": false, "type": "IntPort", "value": 12345}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "time_limits": {"customized": true, "type": "ListPort", "value": [0, -1]}}, "uuid": "41724c90-68be-4118-ac3c-eb5de598f395"}, "node12": {"class": "InsertMarkers", "module": "neuropype.nodes.markers.InsertMarkers", "params": {"anchor_marker": {"customized": true, "type": "Port", "value": "calibration-open"}, "anchor_marker_B": {"customized": true, "type": "Port", "value": "calibration-close"}, "count": {"customized": false, "type": "FloatPort", "value": 1}, "counting": {"customized": true, "type": "EnumPort", "value": "persecond"}, "enforce_intermittent_in": {"customized": false, "type": "EnumPort", "value": "marker-span"}, "except_markers": {"customized": false, "type": "ListPort", "value": []}, "extra_limits": {"customized": false, "type": "ListPort", "value": []}, "instance_fields_from": {"customized": false, "type": "EnumPort", "value": "first"}, "intermittent_markers": {"customized": false, "type": "EnumPort", "value": "allow"}, "marker_format": {"customized": false, "type": "EnumPort", "value": "verbatim"}, "max_length": {"customized": false, "type": "FloatPort", "value": null}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "min_length": {"customized": false, "type": "FloatPort", "value": null}, "mode": {"customized": true, "type": "EnumPort", "value": "marker-spanned"}, "payload": {"customized": true, "type": "Port", "value": "eyes-open"}, "placement": {"customized": false, "type": "EnumPort", "value": "equidistant"}, "random_seed": {"customized": false, "type": "IntPort", "value": 12345}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "time_limits": {"customized": true, "type": "ListPort", "value": [0, -1]}}, "uuid": "51d44fa2-52f6-4b8b-a681-0db811b684ea"}, "node13": {"class": "AssignTargets", "module": "neuropype.nodes.machine_learning.AssignTargets", "params": {"also_legacy_output": {"customized": false, "type": "BoolPort", "value": false}, "is_categorical": {"customized": false, "type": "BoolPort", "value": false}, "iv_column": {"customized": false, "type": "StringPort", "value": "Marker"}, "mapping": {"customized": true, "type": "Port", "value": ["eyes-closed", "eyes-open"]}, "mapping_format": {"customized": false, "type": "EnumPort", "value": "compat"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "support_wildcards": {"customized": false, "type": "BoolPort", "value": false}, "use_numbers": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "7ca2cdd3-1dfc-4d99-8942-81aa7edb8129"}, "node14": {"class": "StripSingletonAxis", "module": "neuropype.nodes.tensor_math.StripSingletonAxis", "params": {"axis": {"customized": false, "type": "EnumPort", "value": "time"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "6f6303cf-2825-4c84-96ab-690ac0ef83c5"}, "node15": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "EnumPort", "value": "frequency"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": "0.5...60"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "Hz"}}, "uuid": "8b625aee-65a1-45c6-a4c7-ee4a5cf5d46f"}, "node16": {"class": "SelectInstances", "module": "neuropype.nodes.formatting.SelectInstances", "params": {"assign_target_value": {"customized": false, "type": "FloatPort", "value": null}, "combine_previous": {"customized": false, "type": "EnumPort", "value": "override"}, "combine_selections": {"customized": false, "type": "EnumPort", "value": "and"}, "condition": {"customized": false, "type": "StringPort", "value": ""}, "default_comparison_operator": {"customized": false, "type": "EnumPort", "value": "auto"}, "drop_immediately": {"customized": false, "type": "BoolPort", "value": true}, "invert_selection": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": {"Marker": ["eyes-closed"]}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "7f6ff240-d5a7-4521-9bb2-aa81be8f4cbe"}, "node17": {"class": "StripSingletonAxis", "module": "neuropype.nodes.tensor_math.StripSingletonAxis", "params": {"axis": {"customized": true, "type": "EnumPort", "value": "instance"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "941e3f5e-011b-45d9-af47-a0f70a0ca95b"}, "node18": {"class": "SelectInstances", "module": "neuropype.nodes.formatting.SelectInstances", "params": {"assign_target_value": {"customized": false, "type": "FloatPort", "value": null}, "combine_previous": {"customized": false, "type": "EnumPort", "value": "override"}, "combine_selections": {"customized": false, "type": "EnumPort", "value": "and"}, "condition": {"customized": false, "type": "StringPort", "value": ""}, "default_comparison_operator": {"customized": false, "type": "EnumPort", "value": "auto"}, "drop_immediately": {"customized": false, "type": "BoolPort", "value": true}, "invert_selection": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": {"Marker": ["eyes-open"]}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "069ea29f-24eb-4778-8abe-d334c3a3eac4"}, "node19": {"class": "StripSingletonAxis", "module": "neuropype.nodes.tensor_math.StripSingletonAxis", "params": {"axis": {"customized": true, "type": "EnumPort", "value": "instance"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "e241d5b8-6213-4843-9d5c-825eeacf4ed6"}, "node2": {"class": "DejitterTimestamps", "module": "neuropype.nodes.utilities.DejitterTimestamps", "params": {"force_monotonic": {"customized": false, "type": "BoolPort", "value": true}, "forget_halftime": {"customized": false, "type": "FloatPort", "value": 90}, "max_updaterate": {"customized": false, "type": "IntPort", "value": 500}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "warmup_samples": {"customized": false, "type": "IntPort", "value": -1}}, "uuid": "e614371d-8f37-4883-abc2-2865b2b03e14"}, "node20": {"class": "GroupedMean", "module": "neuropype.nodes.statistics.GroupedMean", "params": {"allow_markers": {"customized": false, "type": "BoolPort", "value": true}, "ci_range": {"customized": false, "type": "FloatPort", "value": 0.95}, "ddof": {"customized": false, "type": "IntPort", "value": 1}, "equal_var": {"customized": false, "type": "BoolPort", "value": false}, "error_type": {"customized": false, "type": "EnumPort", "value": "none"}, "fill_cols": {"customized": false, "type": "BoolPort", "value": true}, "group_cols": {"customized": true, "type": "ListPort", "value": ["Marker"]}, "grouping_type": {"customized": false, "type": "EnumPort", "value": "levels"}, "mean_type": {"customized": false, "type": "EnumPort", "value": "mean"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": false, "type": "ListPort", "value": [0, 0]}, "use_caching": {"customized": false, "type": "BoolPort", "value": false}, "winsorize": {"customized": true, "type": "BoolPort", "value": false}}, "uuid": "508a8777-950a-425f-9bff-314b32951853"}, "node21": {"class": "SpectrumPlot", "module": "neuropype.nodes.visualization.SpectrumPlot", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": false}, "autoscale": {"customized": true, "type": "BoolPort", "value": false}, "background_color": {"customized": true, "type": "StringPort", "value": "#FFFFFF"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#000000"}, "downsampled": {"customized": false, "type": "BoolPort", "value": false}, "initial_dims": {"customized": true, "type": "ListPort", "value": [620, 10, 600, 500]}, "line_color": {"customized": true, "type": "StringPort", "value": "#000000"}, "line_width": {"customized": false, "type": "FloatPort", "value": 0.75}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "one_over_f_correction": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": true, "type": "FloatPort", "value": 0.01}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stacked": {"customized": true, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "title": {"customized": true, "type": "StringPort", "value": "Spectrum Plot (Eyes Closed)"}, "zero_color": {"customized": false, "type": "StringPort", "value": "#7F7F7F7F"}}, "uuid": "904ad073-554b-4cdf-8d9c-3607b17a8f4e"}, "node22": {"class": "SpectrumPlot", "module": "neuropype.nodes.visualization.SpectrumPlot", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": false}, "autoscale": {"customized": true, "type": "BoolPort", "value": false}, "background_color": {"customized": true, "type": "StringPort", "value": "#FFFFFF"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#000000"}, "downsampled": {"customized": false, "type": "BoolPort", "value": false}, "initial_dims": {"customized": true, "type": "ListPort", "value": [10, 10, 600, 500]}, "line_color": {"customized": true, "type": "StringPort", "value": "#000000"}, "line_width": {"customized": false, "type": "FloatPort", "value": 0.75}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "one_over_f_correction": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": true, "type": "FloatPort", "value": 0.01}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stacked": {"customized": true, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "title": {"customized": true, "type": "StringPort", "value": "Spectrum Plot (Eyes Opened)"}, "zero_color": {"customized": false, "type": "StringPort", "value": "#7F7F7F7F"}}, "uuid": "fb6e3321-ee43-4f82-9865-8b95fb90735c"}, "node23": {"class": "PeakLatency", "module": "neuropype.nodes.signal_processing.PeakLatency", "params": {"account_for_time_axis": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "EnumPort", "value": "frequency"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "negative": {"customized": false, "type": "BoolPort", "value": false}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "subtract_filter_delay": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "Hz"}, "update_on_streaming": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "2990efc4-3df6-4251-8ca4-a252e1040f8c"}, "node24": {"class": "SelectInstances", "module": "neuropype.nodes.formatting.SelectInstances", "params": {"assign_target_value": {"customized": false, "type": "FloatPort", "value": null}, "combine_previous": {"customized": false, "type": "EnumPort", "value": "override"}, "combine_selections": {"customized": false, "type": "EnumPort", "value": "and"}, "condition": {"customized": false, "type": "StringPort", "value": ""}, "default_comparison_operator": {"customized": false, "type": "EnumPort", "value": "auto"}, "drop_immediately": {"customized": false, "type": "BoolPort", "value": true}, "invert_selection": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": {"Marker": ["eyes-closed"]}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "1883f714-3697-46d7-b6ff-2973b9e6ac1c"}, "node25": {"class": "BarPlot", "module": "neuropype.nodes.visualization.BarPlot", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "auto_bar_colors": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "EnumPort", "value": "space"}, "background_color": {"customized": false, "type": "StringPort", "value": "#FFFFFF"}, "bar_color": {"customized": false, "type": "StringPort", "value": "b"}, "bar_width": {"customized": false, "type": "FloatPort", "value": 0.33}, "colormap": {"customized": false, "type": "EnumPort", "value": "turbo"}, "font_size": {"customized": false, "type": "FloatPort", "value": 10.0}, "initial_dims": {"customized": true, "type": "ListPort", "value": [10, 540, 600, 400]}, "instance_field": {"customized": false, "type": "StringPort", "value": null}, "label_rotation": {"customized": true, "type": "EnumPort", "value": "horizontal"}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "title": {"customized": true, "type": "StringPort", "value": "Alpha Peak Frequency | EC - Low Mean (Hz)"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "y_limits": {"customized": true, "type": "ListPort", "value": [5, 40]}}, "uuid": "3bab63c2-03f6-4e04-b065-b258333c19af"}, "node26": {"class": "Mean", "module": "neuropype.nodes.statistics.Mean", "params": {"axis": {"customized": false, "type": "EnumPort", "value": "instance"}, "compute_backend": {"customized": false, "type": "EnumPort", "value": "keep"}, "force_feature_axis": {"customized": false, "type": "BoolPort", "value": false}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "precision": {"customized": false, "type": "EnumPort", "value": "keep"}, "robust": {"customized": false, "type": "BoolPort", "value": false}, "robust_estimator_type": {"customized": false, "type": "EnumPort", "value": "median"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": true, "type": "FloatPort", "value": 0}}, "uuid": "de042a75-599e-45d6-9dcb-51d5435ca38e"}, "node27": {"class": "BarPlot", "module": "neuropype.nodes.visualization.BarPlot", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "auto_bar_colors": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "EnumPort", "value": "space"}, "background_color": {"customized": false, "type": "StringPort", "value": "#FFFFFF"}, "bar_color": {"customized": false, "type": "StringPort", "value": "b"}, "bar_width": {"customized": false, "type": "FloatPort", "value": 0.33}, "colormap": {"customized": false, "type": "EnumPort", "value": "turbo"}, "font_size": {"customized": false, "type": "FloatPort", "value": 10.0}, "initial_dims": {"customized": true, "type": "ListPort", "value": [1150, 200, 700, 500]}, "instance_field": {"customized": false, "type": "StringPort", "value": null}, "label_rotation": {"customized": true, "type": "EnumPort", "value": "horizontal"}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "title": {"customized": true, "type": "StringPort", "value": "Alpha Peak Frequency | EC - Mean (Hz)"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "y_limits": {"customized": true, "type": "ListPort", "value": [5, 40]}}, "uuid": "7503b7ad-4e67-49c7-9e4d-2a3503fc5798"}, "node28": {"class": "Winsorize", "module": "neuropype.nodes.statistics.Winsorize", "params": {"axis": {"customized": false, "type": "EnumPort", "value": "instance"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": true, "type": "FloatPort", "value": 0.3}, "trim_proportion_lower": {"customized": true, "type": "FloatPort", "value": 0.3}}, "uuid": "cdf876c7-a595-4168-a5ce-3c516641d4ee"}, "node29": {"class": "Winsorize", "module": "neuropype.nodes.statistics.Winsorize", "params": {"axis": {"customized": false, "type": "EnumPort", "value": "instance"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": true, "type": "FloatPort", "value": 0.7}, "trim_proportion_lower": {"customized": true, "type": "FloatPort", "value": 0}}, "uuid": "3eb15d6f-aba8-42b4-9084-f428a97e5cce"}, "node3": {"class": "SetAxisValues", "module": "neuropype.nodes.tensor_math.SetAxisValues", "params": {"array_name": {"customized": false, "type": "StringPort", "value": null}, "axis": {"customized": true, "type": "EnumPort", "value": "space"}, "axis_label": {"customized": false, "type": "StringPort", "value": null}, "axis_occurrence": {"customized": false, "type": "IntPort", "value": 0}, "handle_existing": {"customized": false, "type": "EnumPort", "value": "replace-all"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "only_signals": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "values": {"customized": true, "type": "Port", "value": ["fp1", "fp2", "po3", "po4", "p7", "p8", "o1", "o2", "f7", "f8", "f3", "f4", "Pz", "Oz", "p3", "p4"]}}, "uuid": "3066e80b-e4a2-4a0e-b46a-802db98151b5"}, "node30": {"class": "Mean", "module": "neuropype.nodes.statistics.Mean", "params": {"axis": {"customized": false, "type": "EnumPort", "value": "instance"}, "compute_backend": {"customized": false, "type": "EnumPort", "value": "keep"}, "force_feature_axis": {"customized": false, "type": "BoolPort", "value": false}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "precision": {"customized": false, "type": "EnumPort", "value": "keep"}, "robust": {"customized": false, "type": "BoolPort", "value": false}, "robust_estimator_type": {"customized": false, "type": "EnumPort", "value": "median"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": true, "type": "FloatPort", "value": 0}}, "uuid": "51ac9bd0-6479-4bfb-ae16-cb6d4d0ba531"}, "node31": {"class": "BarPlot", "module": "neuropype.nodes.visualization.BarPlot", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "auto_bar_colors": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "EnumPort", "value": "space"}, "background_color": {"customized": false, "type": "StringPort", "value": "#FFFFFF"}, "bar_color": {"customized": false, "type": "StringPort", "value": "b"}, "bar_width": {"customized": false, "type": "FloatPort", "value": 0.33}, "colormap": {"customized": false, "type": "EnumPort", "value": "turbo"}, "font_size": {"customized": false, "type": "FloatPort", "value": 10.0}, "initial_dims": {"customized": true, "type": "ListPort", "value": [620, 540, 600, 400]}, "instance_field": {"customized": false, "type": "StringPort", "value": null}, "label_rotation": {"customized": true, "type": "EnumPort", "value": "horizontal"}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "title": {"customized": true, "type": "StringPort", "value": "Alpha Peak Frequency | EC - High Mean (Hz)"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "y_limits": {"customized": true, "type": "ListPort", "value": [5, 40]}}, "uuid": "6c103687-002f-471a-b290-b75fa0ef4df5"}, "node32": {"class": "Mean", "module": "neuropype.nodes.statistics.Mean", "params": {"axis": {"customized": false, "type": "EnumPort", "value": "instance"}, "compute_backend": {"customized": false, "type": "EnumPort", "value": "keep"}, "force_feature_axis": {"customized": false, "type": "BoolPort", "value": false}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "precision": {"customized": false, "type": "EnumPort", "value": "keep"}, "robust": {"customized": false, "type": "BoolPort", "value": false}, "robust_estimator_type": {"customized": false, "type": "EnumPort", "value": "median"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": true, "type": "FloatPort", "value": 0}}, "uuid": "7b1f66e4-fec0-4585-adef-260f70b0089b"}, "node33": {"class": "Winsorize", "module": "neuropype.nodes.statistics.Winsorize", "params": {"axis": {"customized": false, "type": "EnumPort", "value": "instance"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": false, "type": "FloatPort", "value": 0.1}, "trim_proportion_lower": {"customized": true, "type": "FloatPort", "value": 0.7}}, "uuid": "83fecc9e-4ee8-45c9-80fe-9f4ae26078db"}, "node34": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "EnumPort", "value": "space"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": false, "type": "Port", "value": ":"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "names"}}, "uuid": "66b1871a-9a7a-4de7-9aab-f7afea4e53ac"}, "node35": {"class": "Mean", "module": "neuropype.nodes.statistics.Mean", "params": {"axis": {"customized": true, "type": "EnumPort", "value": "space"}, "compute_backend": {"customized": false, "type": "EnumPort", "value": "keep"}, "force_feature_axis": {"customized": false, "type": "BoolPort", "value": false}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "precision": {"customized": false, "type": "EnumPort", "value": "keep"}, "robust": {"customized": false, "type": "BoolPort", "value": false}, "robust_estimator_type": {"customized": false, "type": "EnumPort", "value": "median"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": true, "type": "FloatPort", "value": 0.2}}, "uuid": "d6f572c8-e00f-48a5-8322-a82b4486c0b4"}, "node36": {"class": "Winsorize", "module": "neuropype.nodes.statistics.Winsorize", "params": {"axis": {"customized": true, "type": "EnumPort", "value": "space"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": true, "type": "FloatPort", "value": 0.2}, "trim_proportion_lower": {"customized": true, "type": "FloatPort", "value": 0.2}}, "uuid": "745d2bc5-7c74-4ccb-bdd8-810304315363"}, "node37": {"class": "InspectPacket", "module": "neuropype.nodes.visualization.InspectPacket", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": true}, "col_axis": {"customized": true, "type": "EnumPort", "value": "none"}, "decimals": {"customized": false, "type": "IntPort", "value": 6}, "every_n_ticks": {"customized": false, "type": "IntPort", "value": 1}, "fewer_buttons": {"customized": false, "type": "BoolPort", "value": false}, "font_size": {"customized": false, "type": "IntPort", "value": 10}, "initial_position": {"customized": true, "type": "ListPort", "value": [1250, 300, 300, 100]}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "row_axis": {"customized": false, "type": "EnumPort", "value": "space"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_axes_table": {"customized": false, "type": "BoolPort", "value": true}, "show_data_table": {"customized": false, "type": "BoolPort", "value": true}, "show_markers_table": {"customized": false, "type": "BoolPort", "value": false}, "show_max_columns": {"customized": false, "type": "IntPort", "value": 20}, "show_max_values": {"customized": false, "type": "IntPort", "value": 50}, "show_streams_table": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": true, "type": "StringPort", "value": "eeg"}, "verbose": {"customized": false, "type": "BoolPort", "value": true}, "window_title": {"customized": true, "type": "StringPort", "value": "Suggested Lower Limit"}}, "uuid": "4edb55e1-a9d2-4704-aaf2-10d4932902d2"}, "node38": {"class": "Mean", "module": "neuropype.nodes.statistics.Mean", "params": {"axis": {"customized": true, "type": "EnumPort", "value": "space"}, "compute_backend": {"customized": false, "type": "EnumPort", "value": "keep"}, "force_feature_axis": {"customized": false, "type": "BoolPort", "value": false}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "precision": {"customized": false, "type": "EnumPort", "value": "keep"}, "robust": {"customized": false, "type": "BoolPort", "value": false}, "robust_estimator_type": {"customized": false, "type": "EnumPort", "value": "median"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": true, "type": "FloatPort", "value": 0.2}}, "uuid": "f66662b5-75a6-4929-881c-844e006ac52a"}, "node39": {"class": "InspectPacket", "module": "neuropype.nodes.visualization.InspectPacket", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": true}, "col_axis": {"customized": true, "type": "EnumPort", "value": "none"}, "decimals": {"customized": false, "type": "IntPort", "value": 6}, "every_n_ticks": {"customized": false, "type": "IntPort", "value": 1}, "fewer_buttons": {"customized": false, "type": "BoolPort", "value": false}, "font_size": {"customized": false, "type": "IntPort", "value": 10}, "initial_position": {"customized": true, "type": "ListPort", "value": [1250, 500, 300, 100]}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "row_axis": {"customized": false, "type": "EnumPort", "value": "space"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_axes_table": {"customized": false, "type": "BoolPort", "value": true}, "show_data_table": {"customized": false, "type": "BoolPort", "value": true}, "show_markers_table": {"customized": false, "type": "BoolPort", "value": false}, "show_max_columns": {"customized": false, "type": "IntPort", "value": 20}, "show_max_values": {"customized": false, "type": "IntPort", "value": 50}, "show_streams_table": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": true, "type": "StringPort", "value": "eeg"}, "verbose": {"customized": false, "type": "BoolPort", "value": true}, "window_title": {"customized": true, "type": "StringPort", "value": "Suggested Upper Limit"}}, "uuid": "3dd32fca-a3c7-4ec1-a33c-ae0dc88b731e"}, "node4": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "EnumPort", "value": "space"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": [2, 3, 4, 5, 6, 7, 12, 13, 14, 15]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": false, "type": "EnumPort", "value": "indices"}}, "uuid": "14c3affc-ba19-48e3-a7cd-90d99a5c3c59"}, "node40": {"class": "Winsorize", "module": "neuropype.nodes.statistics.Winsorize", "params": {"axis": {"customized": true, "type": "EnumPort", "value": "space"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": true, "type": "FloatPort", "value": 0.2}, "trim_proportion_lower": {"customized": true, "type": "FloatPort", "value": 0.2}}, "uuid": "4297dec0-9185-437b-bb92-9c13500aabea"}, "node41": {"class": "ParameterPort", "module": "neuropype.nodes.workflow.ParameterPort", "params": {"autocast": {"customized": false, "type": "BoolPort", "value": true}, "canbenone": {"customized": false, "type": "BoolPort", "value": true}, "default": {"customized": true, "type": "Port", "value": "C:\\bci-control\\bci-study-alpha-waves\\example_data\\alpha_waves_calibration_example.xdf"}, "desc": {"customized": false, "type": "StringPort", "value": ""}, "domain": {"customized": false, "type": "StringPort", "value": null}, "editable": {"customized": false, "type": "BoolPort", "value": true}, "expert": {"customized": false, "type": "BoolPort", "value": false}, "is_filename": {"customized": false, "type": "BoolPort", "value": false}, "is_visible": {"customized": false, "type": "BoolPort", "value": true}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "port_category": {"customized": false, "type": "StringPort", "value": ""}, "portname": {"customized": true, "type": "StringPort", "value": "Filename"}, "relationships": {"customized": false, "type": "ListPort", "value": []}, "safe": {"customized": false, "type": "BoolPort", "value": false}, "select": {"customized": false, "type": "EnumPort", "value": "none"}, "send_signal_changed": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "value_type": {"customized": false, "type": "EnumPort", "value": "string"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "verbose_name": {"customized": false, "type": "StringPort", "value": null}}, "uuid": "df674904-43d5-4933-b210-878201c4049b"}, "node5": {"class": "ScrollPlot", "module": "neuropype.nodes.visualization.ScrollPlot", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "autoscale": {"customized": true, "type": "BoolPort", "value": false}, "background_color": {"customized": false, "type": "StringPort", "value": "#FFFFFF"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#000000"}, "downsampled": {"customized": false, "type": "BoolPort", "value": false}, "initial_dims": {"customized": true, "type": "ListPort", "value": [50, 50, 600, 800]}, "line_color": {"customized": false, "type": "StringPort", "value": "#000000"}, "line_width": {"customized": false, "type": "FloatPort", "value": 0.75}, "marker_color": {"customized": false, "type": "Port", "value": "#FF0000"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nans_as_zero": {"customized": false, "type": "BoolPort", "value": false}, "override_srate": {"customized": false, "type": "FloatPort", "value": null}, "plot_markers": {"customized": false, "type": "BoolPort", "value": true}, "scale": {"customized": true, "type": "FloatPort", "value": 0.1}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "time_range": {"customized": false, "type": "FloatPort", "value": 5.0}, "title": {"customized": true, "type": "StringPort", "value": "Raw Data"}, "zero_color": {"customized": false, "type": "StringPort", "value": "#7F7F7F"}, "zeromean": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "0f5ecea3-38bf-4dfd-9ef0-953af38c6ab0"}, "node6": {"class": "ArtifactRemoval", "module": "neuropype.nodes.neural.ArtifactRemoval", "params": {"a": {"customized": false, "type": "Port", "value": null}, "b": {"customized": false, "type": "Port", "value": null}, "block_size": {"customized": false, "type": "IntPort", "value": null}, "calib_seconds": {"customized": false, "type": "IntPort", "value": 45}, "cutoff": {"customized": false, "type": "FloatPort", "value": 7.5}, "emit_calib_data": {"customized": false, "type": "BoolPort", "value": true}, "init_on": {"customized": false, "type": "ListPort", "value": []}, "lookahead": {"customized": false, "type": "Port", "value": null}, "max_bad_channels": {"customized": false, "type": "FloatPort", "value": 0.2}, "max_dims": {"customized": false, "type": "FloatPort", "value": 0}, "max_dropout_fraction": {"customized": false, "type": "FloatPort", "value": 0.1}, "max_mem": {"customized": true, "type": "Port", "value": 512}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "min_clean_fraction": {"customized": false, "type": "FloatPort", "value": 0.25}, "min_required_channels": {"customized": false, "type": "IntPort", "value": 2}, "preserve_band": {"customized": false, "type": "DictPort", "value": null}, "riemannian": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stddev_cutoff": {"customized": true, "type": "IntPort", "value": 15}, "step_size": {"customized": false, "type": "FloatPort", "value": 0.2}, "use_clean_window": {"customized": false, "type": "BoolPort", "value": true}, "use_legacy": {"customized": true, "type": "BoolPort", "value": false}, "window_len_cleanwindow": {"customized": false, "type": "FloatPort", "value": 0.5}, "window_length": {"customized": false, "type": "FloatPort", "value": 0.5}, "window_overlap": {"customized": false, "type": "FloatPort", "value": 0.66}, "window_overlap_cleanwindow": {"customized": false, "type": "FloatPort", "value": 0.66}, "zscore_thresholds": {"customized": false, "type": "ListPort", "value": [-5, 7]}}, "uuid": "36862da6-5079-4e8f-a6dd-ab8793d51eec"}, "node7": {"class": "ScrollPlot", "module": "neuropype.nodes.visualization.ScrollPlot", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "autoscale": {"customized": false, "type": "BoolPort", "value": true}, "background_color": {"customized": false, "type": "StringPort", "value": "#FFFFFF"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#000000"}, "downsampled": {"customized": false, "type": "BoolPort", "value": false}, "initial_dims": {"customized": true, "type": "ListPort", "value": [700, 50, 600, 800]}, "line_color": {"customized": false, "type": "StringPort", "value": "#000000"}, "line_width": {"customized": false, "type": "FloatPort", "value": 0.75}, "marker_color": {"customized": false, "type": "Port", "value": "#FF0000"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nans_as_zero": {"customized": false, "type": "BoolPort", "value": false}, "override_srate": {"customized": false, "type": "FloatPort", "value": null}, "plot_markers": {"customized": false, "type": "BoolPort", "value": true}, "scale": {"customized": true, "type": "FloatPort", "value": 0.1}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stream_name": {"customized": false, "type": "StringPort", "value": null}, "time_range": {"customized": false, "type": "FloatPort", "value": 5.0}, "title": {"customized": false, "type": "StringPort", "value": "Time series view"}, "zero_color": {"customized": false, "type": "StringPort", "value": "#7F7F7F"}, "zeromean": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "26be8eb5-44de-4f2e-b4fc-59594bdb58ab"}, "node8": {"class": "MultitaperSpectrum", "module": "neuropype.nodes.spectral.MultitaperSpectrum", "params": {"average_over_time_window": {"customized": false, "type": "BoolPort", "value": false}, "half_bandwidth": {"customized": false, "type": "FloatPort", "value": 2.5}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nfft": {"customized": false, "type": "IntPort", "value": null}, "num_tapers": {"customized": false, "type": "IntPort", "value": null}, "onesided": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "200f9db9-985c-40ea-9175-3d4d7070ab75"}, "node9": {"class": "Segmentation", "module": "neuropype.nodes.formatting.Segmentation", "params": {"keep_marker_chunk": {"customized": false, "type": "BoolPort", "value": false}, "max_gap_length": {"customized": true, "type": "FloatPort", "value": 0}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "online_epoching": {"customized": false, "type": "EnumPort", "value": "marker-locked"}, "sample_offset": {"customized": false, "type": "IntPort", "value": 0}, "select_markers": {"customized": false, "type": "ListPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "time_bounds": {"customized": true, "type": "ListPort", "value": [0, 3]}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "964a5d8b-369d-44a2-bba8-88df027200a8"}}, "version": 1.1}</patch>
</scheme>
