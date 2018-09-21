<?xml version='1.0' encoding='utf-8'?>
<scheme description="This pipeline plots the EEG data in the time domain.&#10; &#10;Nodes Description:&#10; &#10;- LSL input: is used to input the streamed data into the pipeline.&#10; &#10;- Dejitter Timestamps: is used to correct timestamps of the data stream, this prevents unwanted behavior in the proceeding nodes.&#10; &#10;- IIR filter: is used to remove the frequency content outside the desired frequency range of typical EEG signal. In this example, we have used a bandpass filter with stopbands from 1-4 Hz and 45-50 Hz.&#10; &#10;- Time Series plot: is used to plot streamed data in the time domain." title="TimeDomain Plotting" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(100, 100)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="0c850c8d-4a5c-49f8-8642-50cb84e56ede" version="1.0.0" />
		<node id="1" name="IIR Filter" position="(300, 100)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter" uuid="b3112038-dbf6-4463-b3e1-53686de691f1" version="1.1.0" />
		<node id="2" name="Time Series Plot" position="(400, 100)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="2c8b1a5b-86eb-4956-b626-8d9358ec6952" version="1.0.0" />
		<node id="3" name="Dejitter Timestamps" position="(200, 100)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="59f0ce51-f896-45ae-bcc5-a00086d6b78a" version="1.0.0" />
		<node id="4" name="Import SET" position="(100, 300)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportset.OWImportSET" title="Import SET" uuid="f3b403ea-7f22-4917-8c37-5f25821ce6e5" version="1.0.0" />
		<node id="5" name="Stream Data" position="(200, 300)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="9b9e293e-2226-4ab9-a5d8-705d404a56f1" version="1.1.0" />
		<node id="6" name="LSL Output" position="(300, 300)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="f2d4be40-f232-48af-bcf8-5d6faa2710be" version="1.0.0" />
		<node id="7" name="Import EDF" position="(92.0, 212.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportedf.OWImportEDF" title="Import EDF" uuid="31bc5e88-ea3e-4d9a-8ae7-6ac440f29d99" version="1.0.0" />
		<node id="8" name="Time Series Plot" position="(193.0, 187.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot (1)" uuid="9a889e26-a29d-4343-a4cf-4454f1ad6dba" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="0" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWBQAAAByZXNvbHZlX21pbmltdW1fdGltZXEBRz/gAAAAAAAAWA0AAABjaGFubmVsX25h
bWVzcQJdcQNYDAAAAG1heF9jaHVua2xlbnEESwBYDAAAAG1heF9ibG9ja2xlbnEFTQAEWAcAAABy
ZWNvdmVycQaIWAoAAABtYXhfYnVmbGVucQdLHlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEIY3Np
cApfdW5waWNrbGVfdHlwZQpxCVgMAAAAUHlRdDQuUXRDb3JlcQpYCgAAAFFCeXRlQXJyYXlxC0Mu
AdnQywABAAAAAAMMAAABWwAABIUAAALZAAADFQAAAYEAAAR8AAAC0AAAAAAAAHEMhXENh3EOUnEP
WAUAAABxdWVyeXEQWBUAAABuYW1lPSdNeU91dHB1dFN0cmVhbSdxEVgMAAAAbm9taW5hbF9yYXRl
cRJYDQAAACh1c2UgZGVmYXVsdClxE1gMAAAAbWFya2VyX3F1ZXJ5cRRYAAAAAHEVWAsAAABkaWFn
bm9zdGljc3EWiXUu
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEsBSwRLLUsyZVgLAAAAaWdub3JlX25hbnNxB4lYBAAAAG1vZGVx
CFgIAAAAYmFuZHBhc3NxCVgQAAAAb2ZmbGluZV9maWx0ZmlsdHEKiVgFAAAAb3JkZXJxC0sAWAkA
AABwYXNzX2xvc3NxDEdACAAAAAAAAFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXENY3NpcApfdW5w
aWNrbGVfdHlwZQpxDlgMAAAAUHlRdDQuUXRDb3JlcQ9YCgAAAFFCeXRlQXJyYXlxEEMuAdnQywAB
AAAAAAMCAAABcgAABGkAAAK8AAADAgAAAYgAAARpAAACvAAAAAAAAHERhXESh3ETUnEUWAoAAABz
dG9wX2F0dGVucRVHQEQAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKIWAsAAABhbnRp
YWxpYXNlZHEDiVgJAAAAYXV0b3NjYWxlcQSIWBAAAABiYWNrZ3JvdW5kX2NvbG9ycQVYBwAAACNG
RkZGRkZxBlgLAAAAZG93bnNhbXBsZWRxB4lYDAAAAGluaXRpYWxfZGltc3EIXXEJWAoAAABsaW5l
X2NvbG9ycQpYBwAAACMwMDAwMDBxC1gMAAAAbWFya2VyX2NvbG9ycQxYBwAAACNGRjAwRkZxDVgM
AAAAbmFuc19hc196ZXJvcQ6JWA4AAABvdmVycmlkZV9zcmF0ZXEPWA0AAAAodXNlIGRlZmF1bHQp
cRBYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEWNzaXAKX3VucGlja2xlX3R5cGUKcRJYDAAAAFB5
UXQ0LlF0Q29yZXETWAoAAABRQnl0ZUFycmF5cRRDLgHZ0MsAAQAAAAADAgAAAUAAAAR7AAADNgAA
AwsAAAFmAAAEcgAAAy0AAAAAAABxFYVxFodxF1JxGFgFAAAAc2NhbGVxGUc/8AAAAAAAAFgLAAAA
c3RyZWFtX25hbWVxGlgAAAAAcRtYCgAAAHRpbWVfcmFuZ2VxHEdAFAAAAAAAAFgFAAAAdGl0bGVx
HVgQAAAAVGltZSBkb21haW4gcGxvdHEeWAoAAAB6ZXJvX2NvbG9ycR9YCQAAACM3RjdGN0Y3RnEg
WAgAAAB6ZXJvbWVhbnEhiHUu
</properties>
		<properties format="literal" node_id="3">{'max_updaterate': 500, 'savedWidgetGeometry': None, 'warmup_samples': -1, 'forget_halftime': 90, 'force_monotonic': True}</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWBEAAABjbG91ZF9jcmVkZW50aWFsc3ED
aAJYCAAAAGZpbGVuYW1lcQRYGQAAAE1vdG9ySW1hZ2VyeVRyYWluVGVzdC5zZXRxBVgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDQuUXRDb3Jl
cQhYCgAAAFFCeXRlQXJyYXlxCUMuAdnQywABAAAAAARDAAAB9QAABbwAAAL1AAAETAAAAhsAAAWz
AAAC7AAAAAAAAHEKhXELh3EMUnENWAwAAABjbG91ZF9idWNrZXRxDmgCWAoAAABjbG91ZF9ob3N0
cQ9YBwAAAERlZmF1bHRxEHUu
</properties>
		<properties format="literal" node_id="5">{'speedup': 1.0, 'looping': True, 'timing': 'wallclock', 'jitter_percent': 5, 'savedWidgetGeometry': None, 'randseed': 34535, 'hitch_probability': 0.0, 'start_pos': 0.0, 'update_interval': 0.04}</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWAsAAABtYXJrZXJfbmFtZXECWBYAAABNeU91dHB1dFN0
cmVhbS1tYXJrZXJzcQNYEAAAAG1hcmtlcl9zb3VyY2VfaWRxBFgAAAAAcQVYDAAAAG1heF9idWZm
ZXJlZHEGSzxYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFuZ2VkcQeJWBMAAABzYXZlZFdpZGdldEdl
b21ldHJ5cQhjc2lwCl91bnBpY2tsZV90eXBlCnEJWAwAAABQeVF0NC5RdENvcmVxClgKAAAAUUJ5
dGVBcnJheXELQy4B2dDLAAEAAAAABEMAAAG3AAAFvAAAAzMAAARMAAAB3QAABbMAAAMqAAAAAAAA
cQyFcQ2HcQ5ScQ9YDAAAAHNlbmRfbWFya2Vyc3EQiFgJAAAAc291cmNlX2lkcRFYFwAAAG15dW5p
cXVlc291cmNlaWQ0NTM0NjM0cRJYBQAAAHNyYXRlcRNYDQAAACh1c2UgZGVmYXVsdClxFFgLAAAA
c3RyZWFtX25hbWVxFVgOAAAATXlPdXRwdXRTdHJlYW1xFlgLAAAAc3RyZWFtX3R5cGVxF1gDAAAA
RUVHcRhYEwAAAHVzZV9kYXRhX3RpbWVzdGFtcHNxGYhYFgAAAHVzZV9udW1weV9vcHRpbWl6YXRp
b25xGol1Lg==
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWEwAAABDOi9Vc2Vycy9zdWhhcy9EZXNrdG9wL3ByanMvZ29sZl9wcm9jZXNz
aW5nL2RhdGEvMDI2MS8wMjYxLzAyNjExMTUwMS5lYnMuZWRmcQhYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxCWNzaXAKX3VucGlja2xlX3R5cGUKcQpYDAAAAFB5UXQ0LlF0Q29yZXELWAoAAABRQnl0
ZUFycmF5cQxDLgHZ0MsAAQAAAAADAwAAAXQAAAR8AAACdAAAAwwAAAGaAAAEcwAAAmsAAAAAAABx
DYVxDodxD1JxEHUu
</properties>
		<properties format="literal" node_id="8">{'absolute_time': False, 'always_on_top': False, 'antialiased': False, 'autoscale': True, 'background_color': '#FFFFFF', 'downsampled': False, 'initial_dims': [50, 50, 700, 500], 'line_color': '#000000', 'marker_color': '#FF00FF', 'nans_as_zero': False, 'override_srate': '(use default)', 'savedWidgetGeometry': None, 'scale': 1.0, 'stream_name': '(use default)', 'time_range': 5.0, 'title': 'Time series view', 'zero_color': '#7F7F7F7F', 'zeromean': True}</properties>
	</node_properties>
	<patch>{
    "edges": [
        [
            "node2",
            "data",
            "node3",
            "data"
        ],
        [
            "node1",
            "data",
            "node4",
            "data"
        ],
        [
            "node1",
            "data",
            "node9",
            "data"
        ],
        [
            "node4",
            "data",
            "node2",
            "data"
        ],
        [
            "node6",
            "data",
            "node7",
            "data"
        ],
        [
            "node8",
            "data",
            "node6",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "F3",
                        "F1",
                        "Fz",
                        "F2",
                        "F4",
                        "C3",
                        "C1",
                        "Cz",
                        "C2",
                        "C4",
                        "CPz",
                        "P3",
                        "P1",
                        "Pz",
                        "P2",
                        "P4",
                        "POz",
                        "O1",
                        "Oz",
                        "O2",
                        "ECG",
                        "AUX1",
                        "AUX2",
                        "AUX3",
                        "ESUTimestamp",
                        "SysTimestamp"
                    ]
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "nominal_rate": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 1024.0
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='MyOutputStream'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                }
            },
            "uuid": "0c850c8d-4a5c-49f8-8642-50cb84e56ede"
        },
        "node2": {
            "class": "IIRFilter",
            "module": "neuropype.nodes.signal_processing.IIRFilter",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "design": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "butter"
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        1,
                        4,
                        45,
                        50
                    ]
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "offline_filtfilt": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "order": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 0
                },
                "pass_loss": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 3.0
                },
                "stop_atten": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 40.0
                }
            },
            "uuid": "b3112038-dbf6-4463-b3e1-53686de691f1"
        },
        "node3": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": []
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "marker_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FF00FF"
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "scale": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.012579115212475336
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": ""
                },
                "time_range": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5.0
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Time domain plot"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "2c8b1a5b-86eb-4956-b626-8d9358ec6952"
        },
        "node4": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 90
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "59f0ce51-f896-45ae-bcc5-a00086d6b78a"
        },
        "node5": {
            "class": "ImportSET",
            "module": "neuropype.nodes.file_system.ImportSET",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "MotorImageryTrainTest.set"
                }
            },
            "uuid": "f3b403ea-7f22-4917-8c37-5f25821ce6e5"
        },
        "node6": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "hitch_probability": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "jitter_percent": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "looping": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 34535
                },
                "speedup": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "start_pos": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timing": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wallclock"
                },
                "update_interval": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.04
                }
            },
            "uuid": "9b9e293e-2226-4ab9-a5d8-705d404a56f1"
        },
        "node7": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "marker_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "MyOutputStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "myuniquesourceid4534634"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "MyOutputStream"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "EEG"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "f2d4be40-f232-48af-bcf8-5d6faa2710be"
        },
        "node8": {
            "class": "ImportEDF",
            "module": "neuropype.nodes.file_system.ImportEDF",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/suhas/Desktop/prjs/golf_processing/data/0261/0261/026111501.ebs.edf"
                }
            },
            "uuid": "31bc5e88-ea3e-4d9a-8ae7-6ac440f29d99"
        },
        "node9": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "marker_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FF00FF"
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "scale": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.0016929977788577967
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5.0
                },
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Time series view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "9a889e26-a29d-4343-a4cf-4454f1ad6dba"
        }
    },
    "version": 1.1
}</patch>
</scheme>
