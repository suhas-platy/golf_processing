<?xml version='1.0' encoding='utf-8'?>
<scheme description="This pipeline can be used to show the spectrum of the EEG data.&#10; &#10;Nodes Description:&#10; &#10;- LSL Input: is used to input the streamed data into the pipeline.&#10; &#10;- Dejitter Timestamps: is used to correct timestamps of the data stream, this prevents unwanted behavior in the proceeding nodes.&#10; &#10;- IIR Filter: is used to highpass filter data to remove the DC component.&#10; &#10;- Moving Window Multitaper Spectrum: is used to calculate the spectrum of the signal using Multitaper method.&#10; &#10;Spectrum plot: is used to plot the spectral content of the signal. This node has an option to compensate for the 1/f fall off inherent in natural signals. This option has been activated for this example." title="Frequency Domain Plotting" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(-500, 100)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="66033ed8-18fe-44bb-a612-560f29cae40a" version="1.0.0" />
		<node id="1" name="IIR Filter" position="(-300, 100)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter" uuid="bc05e953-d573-4bec-8e90-6ff1142452fe" version="1.1.0" />
		<node id="2" name="Spectrum Plot" position="(0, 100)" project_name="NeuroPype" qualified_name="widgets.visualization.owspectrumplot.OWSpectrumPlot" title="Spectrum Plot" uuid="5f8cebdb-b662-427c-a8df-191e579c2fdf" version="1.0.0" />
		<node id="3" name="Dejitter Timestamps" position="(-400, 100)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="b2fcaef6-c709-4285-9584-34dde96223e7" version="1.0.0" />
		<node id="4" name="Import SET" position="(-500, 300)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportset.OWImportSET" title="Import SET" uuid="5ecc2d5a-df09-4f6e-aba8-c6e067d7e1fa" version="1.0.0" />
		<node id="5" name="Stream Data" position="(-400, 300)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="ca3173d0-4835-4b79-947e-53f821501523" version="1.1.0" />
		<node id="6" name="LSL Output" position="(-300, 300)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="ab603980-c6a7-4f35-beb9-a7c9e2c962db" version="1.0.0" />
		<node id="7" name="Moving Window" position="(-200, 100)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owmovingwindow.OWMovingWindow" title="Moving Window" uuid="1524288a-040a-4438-9641-04f01dc29dac" version="1.0.0" />
		<node id="8" name="Power Spectrum (Multitaper)" position="(-100, 100)" project_name="NeuroPype" qualified_name="widgets.spectral.owmultitaperspectrum.OWMultitaperSpectrum" title="Power Spectrum (Multitaper)" uuid="01334d49-5f4c-415e-9bd3-7b3652174c3f" version="1.0.0" />
		<node id="9" name="Import EDF" position="(-506.0, 211.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportedf.OWImportEDF" title="Import EDF" uuid="58dea10b-f0b2-440d-99c7-e327f42ef7e1" version="1.0.0" />
		<node id="10" name="Time Series Plot" position="(-384.0, 211.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="587bfc5e-b65f-4c6a-8d17-a9303fe5f78f" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="0" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWBQAAAByZXNvbHZlX21pbmltdW1fdGltZXEBRz/gAAAAAAAAWA0AAABjaGFubmVsX25h
bWVzcQJdcQNYDAAAAG1heF9jaHVua2xlbnEESwBYDAAAAG5vbWluYWxfcmF0ZXEFWA0AAAAodXNl
IGRlZmF1bHQpcQZYBwAAAHJlY292ZXJxB4hYCgAAAG1heF9idWZsZW5xCEseWAwAAABtYXJrZXJf
cXVlcnlxCVgAAAAAcQpYBQAAAHF1ZXJ5cQtYFQAAAG5hbWU9J015T3V0cHV0U3RyZWFtJ3EMWAwA
AABtYXhfYmxvY2tsZW5xDU0ABFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEOY3NpcApfdW5waWNr
bGVfdHlwZQpxD1gMAAAAUHlRdDQuUXRDb3JlcRBYCgAAAFFCeXRlQXJyYXlxEUMuAdnQywABAAAA
AATeAAABuQAABlcAAAM3AAAE5wAAAd8AAAZOAAADLgAAAAAAAHEShXETh3EUUnEVWAsAAABkaWFn
bm9zdGljc3EWiXUu
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEsBSwJlWAsAAABpZ25vcmVfbmFuc3EHiVgEAAAAbW9kZXEIWAgA
AABoaWdocGFzc3EJWBAAAABvZmZsaW5lX2ZpbHRmaWx0cQqJWAUAAABvcmRlcnELSwBYCQAAAHBh
c3NfbG9zc3EMR0AIAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ1jc2lwCl91bnBpY2ts
ZV90eXBlCnEOWAwAAABQeVF0NC5RdENvcmVxD1gKAAAAUUJ5dGVBcnJheXEQQy4B2dDLAAEAAAAA
AwIAAAFyAAAEaQAAAp0AAAMCAAABiAAABGkAAAKdAAAAAAAAcRGFcRKHcRNScRRYCgAAAHN0b3Bf
YXR0ZW5xFUdARAAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAoAAABsaW5lX2NvbG9ycQFYBwAAACMwMDAwMDBxAlgFAAAAdGl0bGVxA1gNAAAAU3Bl
Y3RydW0gdmlld3EEWAoAAAB6ZXJvX2NvbG9ycQVYCQAAACM3RjdGN0Y3RnEGWBUAAABvbmVfb3Zl
cl9mX2NvcnJlY3Rpb25xB4hYCwAAAHN0cmVhbV9uYW1lcQhYAAAAAHEJWAwAAABpbml0aWFsX2Rp
bXNxCl1xC1gJAAAAYXV0b3NjYWxlcQyIWAcAAABzdGFja2VkcQ2IWA0AAABhbHdheXNfb25fdG9w
cQ6IWBAAAABiYWNrZ3JvdW5kX2NvbG9ycQ9YBwAAACNGRkZGRkZxEFgTAAAAc2F2ZWRXaWRnZXRH
ZW9tZXRyeXERY3NpcApfdW5waWNrbGVfdHlwZQpxElgMAAAAUHlRdDQuUXRDb3JlcRNYCgAAAFFC
eXRlQXJyYXlxFEMuAdnQywABAAAAAAUBAAAB6wAABnoAAAOvAAAFCgAAAhEAAAZxAAADpgAAAAAA
AHEVhXEWh3EXUnEYWAsAAABhbnRpYWxpYXNlZHEZiVgFAAAAc2NhbGVxGkc/8AAAAAAAAFgLAAAA
ZG93bnNhbXBsZWRxG4l1Lg==
</properties>
		<properties format="literal" node_id="3">{'max_updaterate': 500, 'savedWidgetGeometry': None, 'warmup_samples': -1, 'forget_halftime': 90, 'force_monotonic': True}</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWBEAAABjbG91ZF9jcmVkZW50aWFsc3ED
aAJYCAAAAGZpbGVuYW1lcQRYGQAAAE1vdG9ySW1hZ2VyeVRyYWluVGVzdC5zZXRxBVgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDQuUXRDb3Jl
cQhYCgAAAFFCeXRlQXJyYXlxCUMuAdnQywABAAAAAARDAAAB9QAABbwAAAL1AAAETAAAAhsAAAWz
AAAC7AAAAAAAAHEKhXELh3EMUnENWAwAAABjbG91ZF9idWNrZXRxDmgCWAoAAABjbG91ZF9ob3N0
cQ9YBwAAAERlZmF1bHRxEHUu
</properties>
		<properties format="literal" node_id="5">{'speedup': 1.0, 'timing': 'wallclock', 'start_pos': 0.0, 'looping': True, 'savedWidgetGeometry': None, 'randseed': 34535, 'hitch_probability': 0.0, 'jitter_percent': 5, 'update_interval': 0.04}</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWAsAAABtYXJrZXJfbmFtZXECWBYAAABNeU91dHB1dFN0
cmVhbS1tYXJrZXJzcQNYEAAAAG1hcmtlcl9zb3VyY2VfaWRxBFgAAAAAcQVYDAAAAG1heF9idWZm
ZXJlZHEGSzxYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFuZ2VkcQeJWBMAAABzYXZlZFdpZGdldEdl
b21ldHJ5cQhjc2lwCl91bnBpY2tsZV90eXBlCnEJWAwAAABQeVF0NC5RdENvcmVxClgKAAAAUUJ5
dGVBcnJheXELQy4B2dDLAAEAAAAABEMAAAG3AAAFvAAAAzMAAARMAAAB3QAABbMAAAMqAAAAAAAA
cQyFcQ2HcQ5ScQ9YDAAAAHNlbmRfbWFya2Vyc3EQiFgJAAAAc291cmNlX2lkcRFYGAAAAG15dW5p
cXVlc291cmNlaWQwNDUzNjM1N3ESWAUAAABzcmF0ZXETWA0AAAAodXNlIGRlZmF1bHQpcRRYCwAA
AHN0cmVhbV9uYW1lcRVYDgAAAE15T3V0cHV0U3RyZWFtcRZYCwAAAHN0cmVhbV90eXBlcRdYAwAA
AEVFR3EYWBMAAAB1c2VfZGF0YV90aW1lc3RhbXBzcRmIWBYAAAB1c2VfbnVtcHlfb3B0aW1pemF0
aW9ucRqJdS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQFjc2lwCl91bnBpY2tsZV90eXBlCnECWAwA
AABQeVF0NC5RdENvcmVxA1gKAAAAUUJ5dGVBcnJheXEEQy4B2dDLAAEAAAAABEMAAAIpAAAFvAAA
AsEAAARMAAACTwAABbMAAAK4AAAAAAAAcQWFcQaHcQdScQhYBAAAAHVuaXRxCVgHAAAAc2Vjb25k
c3EKWAcAAAB2ZXJib3NlcQuJWA0AAAB3aW5kb3dfbGVuZ3RocQxLA3Uu
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWBgAAABhdmVyYWdlX292ZXJfdGltZV93aW5kb3dxAYlYDgAAAGhhbGZfYmFuZHdpZHRo
cQJHQAQAAAAAAABYBAAAAG5mZnRxA1gNAAAAKHVzZSBkZWZhdWx0KXEEWAoAAABudW1fdGFwZXJz
cQVYDQAAACh1c2UgZGVmYXVsdClxBlgIAAAAb25lc2lkZWRxB4hYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxCGNzaXAKX3VucGlja2xlX3R5cGUKcQlYDAAAAFB5UXQ0LlF0Q29yZXEKWAoAAABRQnl0
ZUFycmF5cQtDLgHZ0MsAAQAAAAAEQwAAAhAAAAW8AAAC2gAABEwAAAI2AAAFswAAAtEAAAAAAABx
DIVxDYdxDlJxD3Uu
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWEwAAABDOi9Vc2Vycy9zdWhhcy9EZXNrdG9wL3ByanMvZ29sZl9wcm9jZXNz
aW5nL2RhdGEvMDI2MS8wMjYxLzAyNjExMTUwMS5lYnMuZWRmcQhYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxCWNzaXAKX3VucGlja2xlX3R5cGUKcQpYDAAAAFB5UXQ0LlF0Q29yZXELWAoAAABRQnl0
ZUFycmF5cQxDLgHZ0MsAAQAAAAADAwAAAXQAAAR8AAACdAAAAwwAAAGaAAAEcwAAAmsAAAAAAABx
DYVxDodxD1JxEHUu
</properties>
		<properties format="literal" node_id="10">{'absolute_time': False, 'always_on_top': False, 'antialiased': False, 'autoscale': True, 'background_color': '#FFFFFF', 'downsampled': False, 'initial_dims': [50, 50, 700, 500], 'line_color': '#000000', 'marker_color': '#FF00FF', 'nans_as_zero': False, 'override_srate': '(use default)', 'savedWidgetGeometry': None, 'scale': 1.0, 'stream_name': '(use default)', 'time_range': 5.0, 'title': 'Time series view', 'zero_color': '#7F7F7F7F', 'zeromean': True}</properties>
	</node_properties>
	<patch>{
    "edges": [
        [
            "node1",
            "data",
            "node4",
            "data"
        ],
        [
            "node1",
            "data",
            "node11",
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
            "node2",
            "data",
            "node8",
            "data"
        ],
        [
            "node8",
            "data",
            "node9",
            "data"
        ],
        [
            "node9",
            "data",
            "node3",
            "data"
        ],
        [
            "node10",
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
            "uuid": "66033ed8-18fe-44bb-a612-560f29cae40a"
        },
        "node10": {
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
            "uuid": "58dea10b-f0b2-440d-99c7-e327f42ef7e1"
        },
        "node11": {
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
                    "value": 0.002925500161866272
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
            "uuid": "587bfc5e-b65f-4c6a-8d17-a9303fe5f78f"
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
                        2
                    ]
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "mode": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "highpass"
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
            "uuid": "bc05e953-d573-4bec-8e90-6ff1142452fe"
        },
        "node3": {
            "class": "SpectrumPlot",
            "module": "neuropype.nodes.visualization.SpectrumPlot",
            "params": {
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
                "one_over_f_correction": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "stacked": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": ""
                },
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Spectrum view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F7F"
                }
            },
            "uuid": "5f8cebdb-b662-427c-a8df-191e579c2fdf"
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
            "uuid": "b2fcaef6-c709-4285-9584-34dde96223e7"
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
            "uuid": "5ecc2d5a-df09-4f6e-aba8-c6e067d7e1fa"
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
            "uuid": "ca3173d0-4835-4b79-947e-53f821501523"
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
                    "value": "myuniquesourceid04536357"
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
            "uuid": "ab603980-c6a7-4f35-beb9-a7c9e2c962db"
        },
        "node8": {
            "class": "MovingWindow",
            "module": "neuropype.nodes.signal_processing.MovingWindow",
            "params": {
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "seconds"
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "window_length": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 3
                }
            },
            "uuid": "1524288a-040a-4438-9641-04f01dc29dac"
        },
        "node9": {
            "class": "MultitaperSpectrum",
            "module": "neuropype.nodes.spectral.MultitaperSpectrum",
            "params": {
                "average_over_time_window": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "half_bandwidth": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2.5
                },
                "nfft": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "num_tapers": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "onesided": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "01334d49-5f4c-415e-9bd3-7b3652174c3f"
        }
    },
    "version": 1.1
}</patch>
</scheme>
