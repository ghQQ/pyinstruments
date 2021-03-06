##### Auto-generated by parse_h_file.py ######### 
from ivi_defines import * 
def add_props(cls): 
    cls._new_attr('cache',                     IVI_ATTR_CACHE                      ,'ViBoolean',False,False,False)
    cls._new_attr('range_check',               IVI_ATTR_RANGE_CHECK                ,'ViBoolean',False,False,False)
    cls._new_attr('query_instrument_status',   IVI_ATTR_QUERY_INSTRUMENT_STATUS    ,'ViBoolean',False,False,False)
    cls._new_attr('record_coercions',          IVI_ATTR_RECORD_COERCIONS           ,'ViBoolean',False,False,False)
    cls._new_attr('simulate',                  IVI_ATTR_SIMULATE                   ,'ViBoolean',False,False,False)
    cls._new_attr('interchange_check',         IVI_ATTR_INTERCHANGE_CHECK          ,'ViBoolean',False,False,False)
    cls._new_attr('spy',                       IVI_ATTR_SPY                        ,'ViBoolean',False,False,False)
    cls._new_attr('use_specific_simulation',   IVI_ATTR_USE_SPECIFIC_SIMULATION    ,'ViBoolean',False,False,False)
    cls._new_attr('group_capabilities',        IVI_ATTR_GROUP_CAPABILITIES         ,'ViString',False,False,True)
    cls._new_attr('function_capabilities',     IVI_ATTR_FUNCTION_CAPABILITIES      ,'ViString',False,False,True)
    cls._new_attr('class_driver_prefix',                         IVI_ATTR_CLASS_DRIVER_PREFIX        ,'ViString',False,False,True)
    cls._new_attr('class_driver_vendor',                         IVI_ATTR_CLASS_DRIVER_VENDOR        ,'ViString',False,False,True)
    cls._new_attr('class_driver_description',                    IVI_ATTR_CLASS_DRIVER_DESCRIPTION   ,'ViString',False,False,True)
    cls._new_attr('class_driver_class_spec_major_version',       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION ,'ViInt32',False,False,True)
    cls._new_attr('class_driver_class_spec_minor_version',       IVI_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION ,'ViInt32',False,False,True)
    cls._new_attr('specific_driver_prefix',                      IVI_ATTR_SPECIFIC_DRIVER_PREFIX     ,'ViString',False,False,True)
    cls._new_attr('specific_driver_locator',                     IVI_ATTR_SPECIFIC_DRIVER_LOCATOR    ,'ViString',False,False,True)
    cls._new_attr('io_resource_descriptor',                      IVI_ATTR_IO_RESOURCE_DESCRIPTOR     ,'ViString',False,False,True)
    cls._new_attr('logical_name',                                IVI_ATTR_LOGICAL_NAME               ,'ViString',False,False,True)
    cls._new_attr('specific_driver_vendor',                      IVI_ATTR_SPECIFIC_DRIVER_VENDOR     ,'ViString',False,False,True)
    cls._new_attr('specific_driver_description',                 IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION,'ViString',False,False,True)
    cls._new_attr('specific_driver_class_spec_major_version',    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION ,'ViInt32',False,False,True)
    cls._new_attr('specific_driver_class_spec_minor_version',    IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION ,'ViInt32',False,False,True)
    cls._new_attr('instrument_firmware_revision',     IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION,'ViString',False,False,True)
    cls._new_attr('instrument_manufacturer',          IVI_ATTR_INSTRUMENT_MANUFACTURER     ,'ViString',False,False,True)
    cls._new_attr('instrument_model',                 IVI_ATTR_INSTRUMENT_MODEL            ,'ViString',False,False,True)
    cls._new_attr('class_driver_revision',            IVI_ATTR_CLASS_DRIVER_REVISION             ,'ViString',False,False,True)
    cls._new_attr('specific_driver_revision',         IVI_ATTR_SPECIFIC_DRIVER_REVISION            ,'ViString',False,False,True)
    cls._new_attr('driver_setup',                     IVI_ATTR_DRIVER_SETUP               ,'ViString',False,False,False)
    cls._new_attr('channel_count',              IVI_ATTR_CHANNEL_COUNT             ,'ViInt32',False,False,True)
    cls._new_attr('output_mode',                (IVI_CLASS_PUBLIC_ATTR_BASE + 1L)  ,'ViInt32',False,False,False)
    cls._new_attr('ref_clock_source',           (IVI_CLASS_PUBLIC_ATTR_BASE + 2L)  ,'ViInt32',False,False,False)
    cls._new_attr('output_enabled',             (IVI_CLASS_PUBLIC_ATTR_BASE + 3L)  ,'ViBoolean',True,False,False)
    cls._new_attr('output_impedance',           (IVI_CLASS_PUBLIC_ATTR_BASE + 4L)  ,'ViReal64',True,False,False)
    cls._new_attr('operation_mode',             (IVI_CLASS_PUBLIC_ATTR_BASE + 5L)  ,'ViInt32',True,False,False)
    cls._new_attr('sample_clock_source',         (IVI_CLASS_PUBLIC_ATTR_BASE + 21L) ,'ViInt32',False,False,False)
    cls._new_attr('sample_clock_output_enabled', (IVI_CLASS_PUBLIC_ATTR_BASE + 22L),'ViBoolean',False,False,False)
    cls._new_attr('terminal_configuration',      (IVI_CLASS_PUBLIC_ATTR_BASE + 31L) ,'ViInt32',True,False,False)
    cls._new_attr('func_waveform',              (IVI_CLASS_PUBLIC_ATTR_BASE + 101L) ,'ViInt32',True,False,False)
    cls._new_attr('func_amplitude',             (IVI_CLASS_PUBLIC_ATTR_BASE + 102L) ,'ViReal64',True,False,False)
    cls._new_attr('func_dc_offset',             (IVI_CLASS_PUBLIC_ATTR_BASE + 103L) ,'ViReal64',True,False,False)
    cls._new_attr('func_frequency',             (IVI_CLASS_PUBLIC_ATTR_BASE + 104L) ,'ViReal64',True,False,False)
    cls._new_attr('func_start_phase',           (IVI_CLASS_PUBLIC_ATTR_BASE + 105L) ,'ViReal64',True,False,False)
    cls._new_attr('func_duty_cycle_high',       (IVI_CLASS_PUBLIC_ATTR_BASE + 106L) ,'ViReal64',True,False,False)
    cls._new_attr('arb_waveform_handle',        (IVI_CLASS_PUBLIC_ATTR_BASE + 201L) ,'ViInt32',True,False,False)
    cls._new_attr('arb_gain',                   (IVI_CLASS_PUBLIC_ATTR_BASE + 202L) ,'ViReal64',True,False,False)
    cls._new_attr('arb_offset',                 (IVI_CLASS_PUBLIC_ATTR_BASE + 203L) ,'ViReal64',True,False,False)
    cls._new_attr('arb_sample_rate',            (IVI_CLASS_PUBLIC_ATTR_BASE + 204L) ,'ViReal64',False,False,False)
    cls._new_attr('max_num_waveforms',          (IVI_CLASS_PUBLIC_ATTR_BASE + 205L) ,'ViInt32',False,False,False)
    cls._new_attr('waveform_quantum',           (IVI_CLASS_PUBLIC_ATTR_BASE + 206L) ,'ViInt32',False,False,False)
    cls._new_attr('min_waveform_size',          (IVI_CLASS_PUBLIC_ATTR_BASE + 207L) ,'ViInt32',False,False,False)
    cls._new_attr('max_waveform_size',          (IVI_CLASS_PUBLIC_ATTR_BASE + 208L) ,'ViInt32',False,False,False)
    cls._new_attr('arb_frequency',              (IVI_CLASS_PUBLIC_ATTR_BASE + 209L) ,'ViReal64',True,False,False)
    cls._new_attr('arb_sequence_handle',        (IVI_CLASS_PUBLIC_ATTR_BASE + 211L) ,'ViInt32',True,False,False)
    cls._new_attr('max_num_sequences',          (IVI_CLASS_PUBLIC_ATTR_BASE + 212L) ,'ViInt32',False,False,False)
    cls._new_attr('min_sequence_length',        (IVI_CLASS_PUBLIC_ATTR_BASE + 213L) ,'ViInt32',False,False,False)
    cls._new_attr('max_sequence_length',        (IVI_CLASS_PUBLIC_ATTR_BASE + 214L) ,'ViInt32',False,False,False)
    cls._new_attr('max_loop_count',             (IVI_CLASS_PUBLIC_ATTR_BASE + 215L) ,'ViInt32',False,False,False)
    cls._new_attr('min_waveform_size64',        (IVI_CLASS_PUBLIC_ATTR_BASE + 221L) ,'ViInt32',False,False,False)
    cls._new_attr('max_waveform_size64',        (IVI_CLASS_PUBLIC_ATTR_BASE + 222L) ,'ViInt32',False,False,False)
    cls._new_attr('binary_alignment',           (IVI_CLASS_PUBLIC_ATTR_BASE + 241L) ,'ViInt32',False,False,False)
    cls._new_attr('output_data_mask',           (IVI_CLASS_PUBLIC_ATTR_BASE + 261L) ,'ViInt32',False,False,False)
    cls._new_attr('sequence_depth_max',         (IVI_CLASS_PUBLIC_ATTR_BASE + 281L) ,'ViInt32',False,False,False)
    cls._new_attr('trigger_source',             (IVI_CLASS_PUBLIC_ATTR_BASE + 302L) ,'ViInt32',True,False,False)
    cls._new_attr('internal_trigger_rate',      (IVI_CLASS_PUBLIC_ATTR_BASE + 310L) ,'ViReal64',False,False,False)
    cls._new_attr('start_trigger_delay',        (IVI_CLASS_PUBLIC_ATTR_BASE + 320L) ,'ViReal64',True,False,False)
    cls._new_attr('start_trigger_slope',        (IVI_CLASS_PUBLIC_ATTR_BASE + 321L) ,'ViInt32',True,False,False)
    cls._new_attr('start_trigger_source',       (IVI_CLASS_PUBLIC_ATTR_BASE + 322L) ,'ViString',True,False,False)
    cls._new_attr('start_trigger_threshold',    (IVI_CLASS_PUBLIC_ATTR_BASE + 323L) ,'ViReal64',True,False,False)
    cls._new_attr('stop_trigger_delay',         (IVI_CLASS_PUBLIC_ATTR_BASE + 330L) ,'ViReal64',True,False,False)
    cls._new_attr('stop_trigger_slope',         (IVI_CLASS_PUBLIC_ATTR_BASE + 331L) ,'ViInt32',True,False,False)
    cls._new_attr('stop_trigger_source',        (IVI_CLASS_PUBLIC_ATTR_BASE + 332L) ,'ViString',True,False,False)
    cls._new_attr('stop_trigger_threshold',     (IVI_CLASS_PUBLIC_ATTR_BASE + 333L) ,'ViReal64',True,False,False)
    cls._new_attr('hold_trigger_delay',         (IVI_CLASS_PUBLIC_ATTR_BASE + 340L) ,'ViReal64',True,False,False)
    cls._new_attr('hold_trigger_slope',         (IVI_CLASS_PUBLIC_ATTR_BASE + 341L) ,'ViInt32',True,False,False)
    cls._new_attr('hold_trigger_source',        (IVI_CLASS_PUBLIC_ATTR_BASE + 342L) ,'ViString',True,False,False)
    cls._new_attr('hold_trigger_threshold',      (IVI_CLASS_PUBLIC_ATTR_BASE + 343L) ,'ViReal64',True,False,False)
    cls._new_attr('burst_count',                (IVI_CLASS_PUBLIC_ATTR_BASE + 350L) ,'ViInt32',True,False,False)
    cls._new_attr('resume_trigger_delay',       (IVI_CLASS_PUBLIC_ATTR_BASE + 360L) ,'ViReal64',True,False,False)
    cls._new_attr('resume_trigger_slope',       (IVI_CLASS_PUBLIC_ATTR_BASE + 361L) ,'ViInt32',True,False,False)
    cls._new_attr('resume_trigger_source',      (IVI_CLASS_PUBLIC_ATTR_BASE + 362L) ,'ViString',True,False,False)
    cls._new_attr('resume_trigger_threshold',   (IVI_CLASS_PUBLIC_ATTR_BASE + 363L) ,'ViReal64',True,False,False)
    cls._new_attr('advance_trigger_delay',      (IVI_CLASS_PUBLIC_ATTR_BASE + 370L) ,'ViReal64',True,False,False)
    cls._new_attr('advance_trigger_slope',      (IVI_CLASS_PUBLIC_ATTR_BASE + 371L) ,'ViInt32',True,False,False)
    cls._new_attr('advance_trigger_source',     (IVI_CLASS_PUBLIC_ATTR_BASE + 372L) ,'ViString',True,False,False)
    cls._new_attr('advance_trigger_threshold',  (IVI_CLASS_PUBLIC_ATTR_BASE + 373L) ,'ViReal64',True,False,False)
    cls._new_attr('am_enabled',                 (IVI_CLASS_PUBLIC_ATTR_BASE + 401L) ,'ViBoolean',True,False,False)
    cls._new_attr('am_source',                  (IVI_CLASS_PUBLIC_ATTR_BASE + 402L) ,'ViInt32',True,False,False)
    cls._new_attr('am_internal_depth',          (IVI_CLASS_PUBLIC_ATTR_BASE + 403L) ,'ViReal64',False,False,False)
    cls._new_attr('am_internal_waveform',       (IVI_CLASS_PUBLIC_ATTR_BASE + 404L) ,'ViInt32',False,False,False)
    cls._new_attr('am_internal_frequency',      (IVI_CLASS_PUBLIC_ATTR_BASE + 405L) ,'ViReal64',False,False,False)
    cls._new_attr('fm_enabled',                 (IVI_CLASS_PUBLIC_ATTR_BASE + 501L) ,'ViBoolean',True,False,False)
    cls._new_attr('fm_source',                  (IVI_CLASS_PUBLIC_ATTR_BASE + 502L) ,'ViInt32',True,False,False)
    cls._new_attr('fm_internal_deviation',      (IVI_CLASS_PUBLIC_ATTR_BASE + 503L) ,'ViReal64',False,False,False)
    cls._new_attr('fm_internal_waveform',       (IVI_CLASS_PUBLIC_ATTR_BASE + 504L) ,'ViInt32',False,False,False)
    cls._new_attr('fm_internal_frequency',      (IVI_CLASS_PUBLIC_ATTR_BASE + 505L) ,'ViReal64',False,False,False)
    cls._new_attr('datamarker_amplitude',       (IVI_CLASS_PUBLIC_ATTR_BASE + 601L) ,'ViReal64',False,False,False)
    cls._new_attr('datamarker_bit_position',    (IVI_CLASS_PUBLIC_ATTR_BASE + 602L) ,'ViInt32',False,False,False)
    cls._new_attr('datamarker_count',           (IVI_CLASS_PUBLIC_ATTR_BASE + 603L) ,'ViInt32',False,False,False)
    cls._new_attr('datamarker_delay',           (IVI_CLASS_PUBLIC_ATTR_BASE + 604L) ,'ViReal64',False,False,False)
    cls._new_attr('datamarker_destination',     (IVI_CLASS_PUBLIC_ATTR_BASE + 605L) ,'ViString',False,False,False)
    cls._new_attr('datamarker_polarity',        (IVI_CLASS_PUBLIC_ATTR_BASE + 606L) ,'ViInt32',False,False,False)
    cls._new_attr('datamarker_source_channel',  (IVI_CLASS_PUBLIC_ATTR_BASE + 607L) ,'ViString',False,False,False)
    cls._new_attr('sparsemarker_amplitude',     (IVI_CLASS_PUBLIC_ATTR_BASE + 701L) ,'ViReal64',True,False,False)
    cls._new_attr('sparsemarker_count',         (IVI_CLASS_PUBLIC_ATTR_BASE + 702L) ,'ViInt32',False,False,False)
    cls._new_attr('sparsemarker_delay',         (IVI_CLASS_PUBLIC_ATTR_BASE + 703L) ,'ViReal64',True,False,False)
    cls._new_attr('sparsemarker_destination',   (IVI_CLASS_PUBLIC_ATTR_BASE + 704L) ,'ViString',True,False,False)
    cls._new_attr('sparsemarker_polarity',      (IVI_CLASS_PUBLIC_ATTR_BASE + 705L) ,'ViInt32',True,False,False)
    cls._new_attr('sparsemarker_wfmhandle',     (IVI_CLASS_PUBLIC_ATTR_BASE + 706L) ,'ViInt32',True,False,False)
