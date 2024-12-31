from oneflux.pipeline.wrappers import Pipeline, PipelineMeteoProc
from oneflux.pipeline.common import ONEFluxPipelineError
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create a minimal config object with required attributes
class DummyConfig(object):
    def get_pipeline_params(self):
        return 'Be-Bra', '20240319', {
            'data_dir': './data',
            'tool_dir': './tools',
            'site_dir': './sites/Be-Bra',
            'first_year': 2000,
            'last_year': 2010,
            'mds-params': {
                'TA': {
                    'tofill': "TA",
                    'driver1': "SW_IN",
                    'driver2a': "TA",
                    'driver2b': "VPD",
                    'tdriver1_min': 20,
                    'tdriver1_max': 50,
                    'tdriver2a_min': 2.5,
                    'tdriver2a_max': 5,
                    'tdriver2b_min': 5,
                    'tdriver2b_max': 10,
                    'odriver1_min': 0,
                    'odriver1_max': 1000,
                    'odriver2a_min': -50,
                    'odriver2a_max': 50,
                    'odriver2b_min': 0,
                    'odriver2b_max': 100
                },
                'SW_IN': {
                    'tofill': "SW_IN",
                    'driver1': "SW_IN", 
                    'driver2a': "TA",
                    'driver2b': "VPD",
                    'tdriver1_min': 20,
                    'tdriver1_max': 50,
                    'tdriver2a_min': 2.5,
                    'tdriver2a_max': 5,
                    'tdriver2b_min': 5,
                    'tdriver2b_max': 10,
                    'odriver1_min': 0,
                    'odriver1_max': 1000,
                    'odriver2a_min': -50,
                    'odriver2a_max': 50,
                    'odriver2b_min': 0,
                    'odriver2b_max': 100
                }
            }
        }
    
    def export_to_yaml(self, dir=None, name=None, is_compact=False):
        # Dummy implementation - does nothing
        pass

    def export_step_to_yaml(self, dir=None):
        # Dummy implementation - does nothing  
        pass

def main():
    # Create pipeline instance with dummy config
    pipeline = Pipeline(DummyConfig())
    #print("\nPipeline configs:")
    #print(pipeline.configs)
    
    # Create meteo_proc instance
    meteo_proc = PipelineMeteoProc(pipeline)
    #print("\nMeteo proc configs:")
    #print(meteo_proc.pipeline.configs)
    
    # Print MDS params specifically
    #print("\nMDS params from config:")
    #print(meteo_proc.pipeline.configs.get('mds-params', 'Not found'))
    
    # Call the method and print result
    mds_params_string = meteo_proc._build_mds_params_string()
    print("\nMDS Parameters String:")
    print(mds_params_string if mds_params_string else "Empty string returned")

if __name__ == '__main__':
    main() 