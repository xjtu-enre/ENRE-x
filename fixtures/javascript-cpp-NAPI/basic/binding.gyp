{
    "targets": [
        # {
        #     "target_name": "addon01",
        #     "sources": [
        #         "example01.cpp"
        #     ]
        # },
        # {
        #     "target_name": "addon02",
        #     "sources": [
        #         "lib/utils.cpp",
        #         "lib/bigNumber.cpp",
        #         "example02.cpp"
        #     ]
        # },
        # {
        #     "target_name": "addon03",
        #     "sources": [
        #         "example03.cpp"
        #     ]
        # },
        # {
        #     "target_name": "addon04",
        #     "sources": [
        #         "example04.cpp"
        #     ]
        # },
        # {
        #     "target_name": "addon05",
        #     "sources": [
        #         "example05.cpp"
        #     ],
        # },
        # {
        #     "target_name": "nan_addon01",
        #     "sources": [
        #         "nan_example01.cpp"
        #     ],
        #     "include_dirs": [
        #         "<!(node -e \"require('nan')\")"
        #     ]
        # },
        # {
        #     "target_name": "nan_addon02",
        #     "sources": [
        #         "nan_example02.cpp"
        #     ],
        #     "include_dirs": [
        #         "<!(node -e \"require('nan')\")"
        #     ]
        # },
        # {
        #     "target_name": "napi_addon01",
        #     "sources": [
        #         "napi_example01.cpp"
        #     ]
        # },
        # {
        #     "target_name": "node_addon_api_addon01",
        #     "include_dirs": [
        #         "<!@(node -p \"require('node-addon-api').include\")"
        #     ],
        #     "dependencies": [
        #         "<!(node -p \"require('node-addon-api').gyp\")"
        #     ],
        #     "cflag!": ["-fno-exceptions"],
        #     "cflag_cc!": ["-fno-exceptions"],
        #     "defines": [
        #         "NAPI_DISABLE_CPP_EXCEPTIONS"
        #     ],
        #     "sources": [
        #         "node_addon_api_example01.cpp"
        #     ]
        # },
        {
            "target_name": "cpp_addon",
            "sources": [
                "main.cpp"
            ]
        },
        {
            "target_name": "napi_example01",
            "sources":[
                "napi_example01.cpp"
            ]
        }
    ]
}
