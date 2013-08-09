"""
a mostly readonly module for the xml file 
C:\\ProgramData\\IVI Foundation\\IVI\\IviConfigurationStore.xml
via the Ivi.ConfigServer.Interop assembly
"""

from pyinstruments.pyhardware.drivers.ivi_interop.ividotnet.dotnet_communication import \
                                            get_config_store, \
                                            get_ivi_driver_session, \
                                            get_ivi_logical_name
from System.Runtime.InteropServices import COMException

def col_to_enum(collection):
    """transforms a driver's collection into a python list"""
    
    return [collection[i+1] for i in range(collection.Count)]

def col_to_dict(collection):
    """transforms a driver's collection into a python dict"""
    
    keys = map(lambda x:x.Name, col_to_enum(collection))
    val = col_to_enum(collection)
    return dict(zip(keys, val))

class pySoftwareModule(object):
    """wrapper class for the xml object"""
    def __init__(self, dotnet_software_module):
        self._sm = dotnet_software_module
        
    @property
    def supported_instrument_models(self):
        """returns a list of strings, that can be compared with the 
        second item after the coma in the *IDN? reply
        """
        
        return self._sm.get_SupportedInstrumentModels().split(",")
    
    @property
    def name(self):
        """returns the name of the SoftwareModule"""
        return self._sm.Name

class ConfigStore(list):
    """the object used to read the xml file."""
    
    def deserialize(self):
        """use this to read from the file"""
        self.__init__()
            
    def __init__(self):
        self._store = get_config_store()
        self._store.Deserialize(self._store.MasterLocation)
        self._add_sessions_and_logical_names()
        super(ConfigStore, self).__init__([pySoftwareModule(sm) \
                            for sm in col_to_enum(self._store.SoftwareModules)])
        
    def _add_sessions_and_logical_names(self):
        """adds a session and a logical_name for all SoftwareModule present in
        the config_store
        """
        
        soft_mods = self._store.SoftwareModules
        soft_mods_dict = col_to_dict(soft_mods)
        sessions = []
        for soft_mod in soft_mods_dict.values():
            name = "pyinstruments_" + soft_mod.Name
            ### adds the driverSession first
            driver_ses = get_ivi_driver_session()
            driver_ses.Name = name
            driver_ses.Description = "entry auto-generated by the python module\
                pyinstruments, beware: edits might be lost!"
            driver_ses.Cache = True
            driver_ses.InterchangeCheck = False
            driver_ses.QueryInstrStatus = False
            driver_ses.RangeCheck = True
            driver_ses.RecordCoercions = False
            driver_ses.Simulate = False
            driver_ses.DriverSetup = ""
            driver_ses.HardwareAsset = None
            driver_ses.SoftwareModule = self._store.SoftwareModules[soft_mod.Name]
            
            ## then adds the logical_name
            log_name = get_ivi_logical_name()
            log_name.Name = name
            log_name.Description = "entry auto-generated by the python module\
                pyinstruments, beware: edits might be lost!"
            
            
            
            if name in col_to_dict(self._store.LogicalNames).keys():
                self._store.LogicalNames.Remove(name)
            if name in col_to_dict(self._store.DriverSessions).keys():
                self._store.DriverSessions.Remove(name)
            if name in col_to_dict(self._store.Sessions).keys():
                self._store.Sessions.Remove(name)
            self._store.DriverSessions.Add(driver_ses)
            log_name.Session = driver_ses
            self._store.LogicalNames.Add(log_name)
        self._store.Serialize(self._store.MasterLocation)
    
    ##============================================================
    ##  remove entries
    ##============================================================
#    def remove_all(self):
#        """removes everythings from the file except for the SoftwareModules"""
#        for i in self.logical_names():
#            self.remove_logical_name(i, False)
#        for i in self.sessions():
#            self.remove_driver_session(i, False)
#        for i in self.hardware_assets():
#            self.remove_ha(i,False)
#        self._store.Serialize(self._store.MasterLocation)

    def get_sm_for_model(self, model):
        """returns the list of SoftwareModules supporting a given 
        model
        """
        
        ret = []
        for i in self:
            if model in i.supported_instrument_models:
                ret.append(i)
        return ret

    def get_supported_models(self, software_module):
        ret = []
        for soft_mod in self:
            if soft_mod.name == software_module:
                return soft_mod.supported_instrument_models
        return []
        
    def get_software_modules(self, instrument_type):
        """
        return all the software module names that support an instrument
        type
        """

        mods = []
        for soft_mod in self:
            for index in range(soft_mod._sm.PublishedAPIs.get_Count()):
                try:
                    papi = soft_mod._sm.PublishedAPIs.\
                                        get_Item(index + 1,0,0,"")
                    if(papi.Name == instrument_type):
                        if(papi.Type == "IVI-COM"):
                            mods.append(soft_mod.name)
                except COMException, AttributeError:
                    pass
        return mods
    
CONFIG_STORE = ConfigStore()