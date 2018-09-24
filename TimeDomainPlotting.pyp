<?xml version='1.0' encoding='utf-8'?>
<scheme description="This pipeline plots the EEG data in the time domain.&#10; &#10;Nodes Description:&#10; &#10;- LSL input: is used to input the streamed data into the pipeline.&#10; &#10;- Dejitter Timestamps: is used to correct timestamps of the data stream, this prevents unwanted behavior in the proceeding nodes.&#10; &#10;- IIR filter: is used to remove the frequency content outside the desired frequency range of typical EEG signal. In this example, we have used a bandpass filter with stopbands from 1-4 Hz and 45-50 Hz.&#10; &#10;- Time Series plot: is used to plot streamed data in the time domain." title="TimeDomain Plotting" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(100, 100)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="33af341f-d409-4145-9b88-2eb6690a499d" version="1.0.0" />
		<node id="1" name="IIR Filter" position="(300, 100)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter" uuid="34ad23d4-ebed-4a92-97f2-4225cf50b5a1" version="1.1.0" />
		<node id="2" name="Time Series Plot" position="(400, 100)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="53f5e453-efed-4f01-a1bd-24a3d6abd013" version="1.0.0" />
		<node id="3" name="Dejitter Timestamps" position="(200, 100)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="3604933c-e64c-4fd4-a026-8074068fd6e4" version="1.0.0" />
		<node id="4" name="Stream Data" position="(200, 300)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="2728ed4a-c9a3-4e70-8fef-2be7f8a7c73f" version="1.1.0" />
		<node id="5" name="LSL Output" position="(421.0, 300.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="d327e8d4-a1db-4743-8195-0ec97cb70d06" version="1.0.0" />
		<node id="6" name="Import EDF" position="(92.0, 212.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportedf.OWImportEDF" title="Import EDF" uuid="7f7cacc9-b50a-42c8-8157-3c7870286274" version="1.0.0" />
		<node id="7" name="Time Series Plot" position="(193.0, 187.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot (1)" uuid="4aec1d2c-2a81-49df-a62d-fe700f5866e0" version="1.0.0" />
		<node id="8" name="Select Range" position="(123.0, 335.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="dbae84c4-cdc5-4294-8f97-8d5e3ed3c566" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="8" />
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
		<properties format="literal" node_id="4">{'speedup': 1.0, 'looping': True, 'timing': 'wallclock', 'jitter_percent': 5, 'savedWidgetGeometry': None, 'randseed': 34535, 'hitch_probability': 0.0, 'start_pos': 0.0, 'update_interval': 0.04}</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWAsAAABtYXJrZXJfbmFtZXECWBYAAABNeU91dHB1dFN0
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
		<properties format="pickle" node_id="6">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWEwAAABDOi9Vc2Vycy9zdWhhcy9EZXNrdG9wL3ByanMvZ29sZl9wcm9jZXNz
aW5nL2RhdGEvMDI2MS8wMjYxLzAyNjExMTUwMS5lYnMuZWRmcQhYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxCWNzaXAKX3VucGlja2xlX3R5cGUKcQpYDAAAAFB5UXQ0LlF0Q29yZXELWAoAAABRQnl0
ZUFycmF5cQxDLgHZ0MsAAQAAAAADAwAAAXQAAAR8AAACdAAAAwwAAAGaAAAEcwAAAmsAAAAAAABx
DYVxDodxD1JxEHUu
</properties>
		<properties format="literal" node_id="7">{'absolute_time': False, 'always_on_top': False, 'antialiased': False, 'autoscale': True, 'background_color': '#FFFFFF', 'downsampled': False, 'initial_dims': [50, 50, 700, 500], 'line_color': '#000000', 'marker_color': '#FF00FF', 'nans_as_zero': False, 'override_srate': '(use default)', 'savedWidgetGeometry': None, 'scale': 1.0, 'stream_name': '(use default)', 'time_range': 5.0, 'title': 'Time series view', 'zero_color': '#7F7F7F7F', 'zeromean': True}</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAADAwAAAYIAAAR8AAACZgAAAwwA
AAGoAAAEcwAAAl0AAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxYAwAAADotNnENWAQA
AAB1bml0cQ5YBwAAAGluZGljZXNxD3Uu
</properties>
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
            "node8",
            "data"
        ],
        [
            "node4",
            "data",
            "node2",
            "data"
        ],
        [
            "node5",
            "data",
            "node6",
            "data"
        ],
        [
            "node7",
            "data",
            "node9",
            "data"
        ],
        [
            "node9",
            "data",
            "node5",
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
                        "O2"
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
            "uuid": "33af341f-d409-4145-9b88-2eb6690a499d"
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
            "uuid": "34ad23d4-ebed-4a92-97f2-4225cf50b5a1"
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
                    "value": 0.07788656582264941
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
            "uuid": "53f5e453-efed-4f01-a1bd-24a3d6abd013"
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
            "uuid": "3604933c-e64c-4fd4-a026-8074068fd6e4"
        },
        "node5": {
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
            "uuid": "2728ed4a-c9a3-4e70-8fef-2be7f8a7c73f"
        },
        "node6": {
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
            "uuid": "d327e8d4-a1db-4743-8195-0ec97cb70d06"
        },
        "node7": {
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
            "uuid": "7f7cacc9-b50a-42c8-8157-3c7870286274"
        },
        "node8": {
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
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
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
            "uuid": "4aec1d2c-2a81-49df-a62d-fe700f5866e0"
        },
        "node9": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": ":-6"
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "dbae84c4-cdc5-4294-8f97-8d5e3ed3c566"
        }
    },
    "version": 1.1
}</patch>
</scheme>
