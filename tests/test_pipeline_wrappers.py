from __future__ import absolute_import

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from oneflux.pipeline.wrappers import PipelineMeteoProc

def test_build_mds_params_string():
    # Create minimal pipeline mock object with configs
    class MockPipeline(object):  # explicitly inherit from object for Python 2
        def __init__(self):
            self.configs = {
                '07_meteo_proc': {
                    'mds-params': {
                        'TA': {
                            'tofill': 'TA',
                            'driver1': 'SW_IN',
                            'driver2a': 'TA',
                            'driver2b': 'VPD',
                            'tdriver1_min': 20,
                            'tdriver1_max': 50,
                            'tdriver2a_min': 2.5,
                            'tdriver2a_max': 5,
                            'tdriver2b_min': 5,
                            'tdriver2b_max': 10,
                            'odriver1_min': 0,
                            'odriver1_max': 1000,
                            'odriver2a_min': 0,
                            'odriver2a_max': 100,
                            'odriver2b_min': 0,
                            'odriver2b_max': 100
                        }
                    }
                }
            }

    # Initialize PipelineMeteoProc with mock pipeline
    pipeline = MockPipeline()
    meteo_proc = PipelineMeteoProc(pipeline)

    # Call the method
    result = meteo_proc._build_mds_params_string()

    # Verify the result contains expected parameters
    assert '-TA_driver1=SW_IN' in result
    assert '-TA_driver2a=TA' in result
    assert '-TA_driver2b=VPD' in result
    assert '-TA_driver1_oor=0,1000' in result
    assert '-TA_tdriver1=20,50' in result
    assert '-TA_tdriver2a=2.5,5' in result
    assert '-TA_tdriver2b=5,10' in result 