class IceFeature(object):
    
    def __init__(self):
        
        self.gmlId = None
        self.geometry = None
        
    def get_geometry(self):
        return self.__geometry
    
    def set_geometry(self, value):   
        self.__geometry = value
    

    def get_gml_id(self):
        return self.__gmlId


    def set_gml_id(self, value):
        self.__gmlId = value

    gmlId = property(get_gml_id, set_gml_id, None, None)

class Seaice(IceFeature):
    
    def __init__(self):
        
        IceFeature.__init__(self)
        
        self.iceact = None 
        self.iceapc = None
        self.icesod = None
        self.iceflz = None
        self.icespc = None
        self.icelvl = None
        self.icecst = None
        self.icefty = None
        self.icedsp = None
        self.iceddr = None
        self.icercn = None
        self.icerfq = None
        self.icermh = None
        self.icerxh = None
        self.icerdv = None
        self.icekcn = None
        self.icekfq = None
        self.icekmd = None
        self.icekxd = None
        self.icefcn = None
        self.icetck = None
        self.icemax = None
        self.icemin = None
        self.icetty = None
        self.icemlt = None
        self.icescn = None
        self.icesct = None
        self.icedos = None
        self.icelst = None
        self.icelfq = None
        self.icelor = None
        self.icelwd = None
        self.ia_sfa = None
        self.ia_sfb = None
        self.ia_sfc = None
        self.ia_ffa = None
        self.ia_ffb = None
        self.ia_ffc = None
        self.ia_sng = None
        self.ia_mlt = None
        self.ia_plg = None
        self.ia_hlg = None
        self.ia_dug = None

    def get_iceact(self):
        return self.__iceact


    def get_iceapc(self):
        return self.__iceapc


    def get_icesod(self):
        return self.__icesod


    def get_iceflz(self):
        return self.__iceflz


    def get_icespc(self):
        return self.__icespc


    def get_icelvl(self):
        return self.__icelvl


    def get_icecst(self):
        return self.__icecst


    def get_icefty(self):
        return self.__icefty


    def get_icedsp(self):
        return self.__icedsp


    def get_iceddr(self):
        return self.__iceddr


    def get_icercn(self):
        return self.__icercn


    def get_icerfq(self):
        return self.__icerfq


    def get_icermh(self):
        return self.__icermh


    def get_icerxh(self):
        return self.__icerxh


    def get_icerdv(self):
        return self.__icerdv


    def get_icekcn(self):
        return self.__icekcn


    def get_icekfq(self):
        return self.__icekfq


    def get_icekmd(self):
        return self.__icekmd


    def get_icekxd(self):
        return self.__icekxd


    def get_icefcn(self):
        return self.__icefcn


    def get_icetck(self):
        return self.__icetck


    def get_icemax(self):
        return self.__icemax


    def get_icemin(self):
        return self.__icemin


    def get_icetty(self):
        return self.__icetty


    def get_icemlt(self):
        return self.__icemlt


    def get_icescn(self):
        return self.__icescn


    def get_icesct(self):
        return self.__icesct


    def get_icedos(self):
        return self.__icedos


    def get_icelst(self):
        return self.__icelst


    def get_icelfq(self):
        return self.__icelfq


    def get_icelor(self):
        return self.__icelor


    def get_icelwd(self):
        return self.__icelwd


    def get_ia_sfa(self):
        return self.__ia_sfa


    def get_ia_sfb(self):
        return self.__ia_sfb


    def get_ia_sfc(self):
        return self.__ia_sfc


    def get_ia_ffa(self):
        return self.__ia_ffa


    def get_ia_ffb(self):
        return self.__ia_ffb


    def get_ia_ffc(self):
        return self.__ia_ffc


    def get_ia_sng(self):
        return self.__ia_sng


    def get_ia_mlt(self):
        return self.__ia_mlt


    def get_ia_plg(self):
        return self.__ia_plg


    def get_ia_hlg(self):
        return self.__ia_hlg


    def get_ia_dug(self):
        return self.__ia_dug


    def set_iceact(self, value):
        self.__iceact = value


    def set_iceapc(self, value):
        self.__iceapc = value


    def set_icesod(self, value):
        self.__icesod = value


    def set_iceflz(self, value):
        self.__iceflz = value


    def set_icespc(self, value):
        self.__icespc = value


    def set_icelvl(self, value):
        self.__icelvl = value


    def set_icecst(self, value):
        self.__icecst = value


    def set_icefty(self, value):
        self.__icefty = value


    def set_icedsp(self, value):
        self.__icedsp = value


    def set_iceddr(self, value):
        self.__iceddr = value


    def set_icercn(self, value):
        self.__icercn = value


    def set_icerfq(self, value):
        self.__icerfq = value


    def set_icermh(self, value):
        self.__icermh = value


    def set_icerxh(self, value):
        self.__icerxh = value


    def set_icerdv(self, value):
        self.__icerdv = value


    def set_icekcn(self, value):
        self.__icekcn = value


    def set_icekfq(self, value):
        self.__icekfq = value


    def set_icekmd(self, value):
        self.__icekmd = value


    def set_icekxd(self, value):
        self.__icekxd = value


    def set_icefcn(self, value):
        self.__icefcn = value


    def set_icetck(self, value):
        self.__icetck = value


    def set_icemax(self, value):
        self.__icemax = value


    def set_icemin(self, value):
        self.__icemin = value


    def set_icetty(self, value):
        self.__icetty = value


    def set_icemlt(self, value):
        self.__icemlt = value


    def set_icescn(self, value):
        self.__icescn = value


    def set_icesct(self, value):
        self.__icesct = value


    def set_icedos(self, value):
        self.__icedos = value


    def set_icelst(self, value):
        self.__icelst = value


    def set_icelfq(self, value):
        self.__icelfq = value


    def set_icelor(self, value):
        self.__icelor = value


    def set_icelwd(self, value):
        self.__icelwd = value


    def set_ia_sfa(self, value):
        self.__ia_sfa = value


    def set_ia_sfb(self, value):
        self.__ia_sfb = value


    def set_ia_sfc(self, value):
        self.__ia_sfc = value


    def set_ia_ffa(self, value):
        self.__ia_ffa = value


    def set_ia_ffb(self, value):
        self.__ia_ffb = value


    def set_ia_ffc(self, value):
        self.__ia_ffc = value


    def set_ia_sng(self, value):
        self.__ia_sng = value


    def set_ia_mlt(self, value):
        self.__ia_mlt = value


    def set_ia_plg(self, value):
        self.__ia_plg = value


    def set_ia_hlg(self, value):
        self.__ia_hlg = value


    def set_ia_dug(self, value):
        self.__ia_dug = value

class Lacice(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.iceact = None
        self.iceapc = None
        self.icelso = None
        self.iceflz = None
        self.icespc = None
        self.icelvl = None
        self.icecst = None
        self.icefty = None
        self.icedsp = None
        self.iceddr = None
        self.icercn = None
        self.icerfq = None
        self.icermh = None
        self.icerxh = None
        self.icerdv = None
        self.icekcn = None
        self.icekfq = None
        self.icekmd = None
        self.icekxd = None
        self.icefcn = None
        self.icetck = None
        self.icemax = None
        self.icemin = None
        self.icetty = None
        self.icemlt = None
        self.icescn = None
        self.icesct = None
        self.icedos = None
        self.icelst = None
        self.icelfq = None
        self.icelor = None
        self.icelwd = None

    def get_iceact(self):
        return self.__iceact


    def get_iceapc(self):
        return self.__iceapc


    def get_icelso(self):
        return self.__icelso


    def get_iceflz(self):
        return self.__iceflz


    def get_icespc(self):
        return self.__icespc


    def get_icelvl(self):
        return self.__icelvl


    def get_icecst(self):
        return self.__icecst


    def get_icefty(self):
        return self.__icefty


    def get_icedsp(self):
        return self.__icedsp


    def get_iceddr(self):
        return self.__iceddr


    def get_icercn(self):
        return self.__icercn


    def get_icerfq(self):
        return self.__icerfq


    def get_icermh(self):
        return self.__icermh


    def get_icerxh(self):
        return self.__icerxh


    def get_icerdv(self):
        return self.__icerdv


    def get_icekcn(self):
        return self.__icekcn


    def get_icekfq(self):
        return self.__icekfq


    def get_icekmd(self):
        return self.__icekmd


    def get_icekxd(self):
        return self.__icekxd


    def get_icefcn(self):
        return self.__icefcn


    def get_icetck(self):
        return self.__icetck


    def get_icemax(self):
        return self.__icemax


    def get_icemin(self):
        return self.__icemin


    def get_icetty(self):
        return self.__icetty


    def get_icemlt(self):
        return self.__icemlt


    def get_icescn(self):
        return self.__icescn


    def get_icesct(self):
        return self.__icesct


    def get_icedos(self):
        return self.__icedos


    def get_icelst(self):
        return self.__icelst


    def get_icelfq(self):
        return self.__icelfq


    def get_icelor(self):
        return self.__icelor


    def get_icelwd(self):
        return self.__icelwd


    def set_iceact(self, value):
        self.__iceact = value


    def set_iceapc(self, value):
        self.__iceapc = value


    def set_icelso(self, value):
        self.__icelso = value


    def set_iceflz(self, value):
        self.__iceflz = value


    def set_icespc(self, value):
        self.__icespc = value


    def set_icelvl(self, value):
        self.__icelvl = value


    def set_icecst(self, value):
        self.__icecst = value


    def set_icefty(self, value):
        self.__icefty = value


    def set_icedsp(self, value):
        self.__icedsp = value


    def set_iceddr(self, value):
        self.__iceddr = value


    def set_icercn(self, value):
        self.__icercn = value


    def set_icerfq(self, value):
        self.__icerfq = value


    def set_icermh(self, value):
        self.__icermh = value


    def set_icerxh(self, value):
        self.__icerxh = value


    def set_icerdv(self, value):
        self.__icerdv = value


    def set_icekcn(self, value):
        self.__icekcn = value


    def set_icekfq(self, value):
        self.__icekfq = value


    def set_icekmd(self, value):
        self.__icekmd = value


    def set_icekxd(self, value):
        self.__icekxd = value


    def set_icefcn(self, value):
        self.__icefcn = value


    def set_icetck(self, value):
        self.__icetck = value


    def set_icemax(self, value):
        self.__icemax = value


    def set_icemin(self, value):
        self.__icemin = value


    def set_icetty(self, value):
        self.__icetty = value


    def set_icemlt(self, value):
        self.__icemlt = value


    def set_icescn(self, value):
        self.__icescn = value


    def set_icesct(self, value):
        self.__icesct = value


    def set_icedos(self, value):
        self.__icedos = value


    def set_icelst(self, value):
        self.__icelst = value


    def set_icelfq(self, value):
        self.__icelfq = value


    def set_icelor(self, value):
        self.__icelor = value


    def set_icelwd(self, value):
        self.__icelwd = value

class Brgare(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.icebnm = None
        self.icebsz = None
        self.ia_bcn = None
        self.ia_bfm = None
        self.ia_buh = None
        

    def get_icebnm(self):
        return self.__icebnm


    def get_icebsz(self):
        return self.__icebsz


    def get_ia_bcn(self):
        return self.__ia_bcn


    def get_ia_bfm(self):
        return self.__ia_bfm


    def get_ia_buh(self):
        return self.__ia_buh


    

    def set_icebnm(self, value):
        self.__icebnm = value


    def set_icebsz(self, value):
        self.__icebsz = value


    def set_ia_bcn(self, value):
        self.__ia_bcn = value


    def set_ia_bfm(self, value):
        self.__ia_bfm = value


    def set_ia_buh(self, value):
        self.__ia_buh = value

class Icelne(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        
class Brglne(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        
class Opnlne(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        
class Lkilne(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        
class I_Ridg(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.icerdv = None
        self.icermh = None
        self.icerxh = None
        

    def get_icerdv(self):
        return self.__icerdv


    def get_icermh(self):
        return self.__icermh


    def get_icerxh(self):
        return self.__icerxh


    

    def set_icerdv(self, value):
        self.__icerdv = value


    def set_icermh(self, value):
        self.__icermh = value


    def set_icerxh(self, value):
        self.__icerxh = value

class I_Lead(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.icesod = None
        self.ia_obn = None
        self.icedvw = None
        self.ia_dmw = None
        self.ia_dxw = None
        

    def get_icesod(self):
        return self.__icesod


    def get_ia_obn(self):
        return self.__ia_obn


    def get_icedvw(self):
        return self.__icedvw


    def get_ia_dmw(self):
        return self.__ia_dmw


    def get_ia_dxw(self):
        return self.__ia_dxw


    

    def set_icesod(self, value):
        self.__icesod = value


    def set_ia_obn(self, value):
        self.__ia_obn = value


    def set_icedvw(self, value):
        self.__icedvw = value


    def set_ia_dmw(self, value):
        self.__ia_dmw = value


    def set_ia_dxw(self, value):
        self.__ia_dxw = value

class I_Fral(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.icesod = None
        self.ia_obn = None
        self.icedvw = None
        self.ia_dmw = None
        self.ia_dxw = None
        

    def get_icesod(self):
        return self.__icesod


    def get_ia_obn(self):
        return self.__ia_obn


    def get_icedvw(self):
        return self.__icedvw


    def get_ia_dmw(self):
        return self.__ia_dmw


    def get_ia_dxw(self):
        return self.__ia_dxw


    

    def set_icesod(self, value):
        self.__icesod = value


    def set_ia_obn(self, value):
        self.__ia_obn = value


    def set_icedvw(self, value):
        self.__icedvw = value


    def set_ia_dmw(self, value):
        self.__ia_dmw = value


    def set_ia_dxw(self, value):
        self.__ia_dxw = value

class I_Crac(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.icesod = None
        self.ia_obn = None
        self.icedvw = None
        self.ia_dmw = None
        self.ia_dxw = None
        

    def get_icesod(self):
        return self.__icesod


    def get_ia_obn(self):
        return self.__ia_obn


    def get_icedvw(self):
        return self.__icedvw


    def get_ia_dmw(self):
        return self.__ia_dmw


    def get_ia_dxw(self):
        return self.__ia_dxw


    

    def set_icesod(self, value):
        self.__icesod = value


    def set_ia_obn(self, value):
        self.__ia_obn = value


    def set_icedvw(self, value):
        self.__icedvw = value


    def set_ia_dmw(self, value):
        self.__ia_dmw = value


    def set_ia_dxw(self, value):
        self.__ia_dxw = value

class Icecom(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.icecst = None
        

    def get_icecst(self):
        return self.__icecst


    

    def set_icecst(self, value):
        self.__icecst = value

class Icelea(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.iceloc = None
        self.icelst = None
        self.icelwd = None
        
    def get_iceloc(self):
        return self.__iceloc


    def get_icelst(self):
        return self.__icelst


    def get_icelwd(self):
        return self.__icelwd


    

    def set_iceloc(self, value):
        self.__iceloc = value


    def set_icelst(self, value):
        self.__icelst = value


    def set_icelwd(self, value):
        self.__icelwd = value

class Icebrg(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.icebsz = None
        self.icedsp = None
        self.iceddr = None
        self.ia_obn = None
        self.ia_bfm = None
        self.ia_buh = None
        

    def get_icebsz(self):
        return self.__icebsz


    def get_icedsp(self):
        return self.__icedsp


    def get_iceddr(self):
        return self.__iceddr


    def get_ia_obn(self):
        return self.__ia_obn


    def get_ia_bfm(self):
        return self.__ia_bfm


    def get_ia_buh(self):
        return self.__ia_buh


    

    def set_icebsz(self, value):
        self.__icebsz = value


    def set_icedsp(self, value):
        self.__icedsp = value


    def set_iceddr(self, value):
        self.__iceddr = value


    def set_ia_obn(self, value):
        self.__ia_obn = value


    def set_ia_bfm(self, value):
        self.__ia_bfm = value


    def set_ia_buh(self, value):
        self.__ia_buh = value

class Flobrg(IceFeature):
        
    def __init__(self):
        
        IceFeature.__init__(self)    
        self.icedsp = None
        self.iceddr = None
        

    def get_icedsp(self):
        return self.__icedsp


    def get_iceddr(self):
        return self.__iceddr


    

    def set_icedsp(self, value):
        self.__icedsp = value


    def set_iceddr(self, value):
        self.__iceddr = value

class Icethk(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.icetck = None
        self.icemax = None
        self.icemin = None
        self.icetty = None
        
        
        
    
        
    def get_icetck(self):
        return self.__icetck


    def get_icemax(self):
        return self.__icemax


    def get_icemin(self):
        return self.__icemin


    def get_icetty(self):
        return self.__icetty


    def set_icetck(self, value):
        self.__icetck = value


    def set_icemax(self, value):
        self.__icemax = value


    def set_icemin(self, value):
        self.__icemin = value


    def set_icetty(self, value):
        self.__icetty = value

class Iceshr(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        
class Icediv(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        
class Icerdg(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.icercn = None
        self.icerfq = None
        self.icermh = None
        self.icerxh = None
        self.icerdv = None
        

    def get_icercn(self):
        return self.__icercn


    def get_icerfq(self):
        return self.__icerfq


    def get_icermh(self):
        return self.__icermh


    def get_icerxh(self):
        return self.__icerxh


    def get_icerdv(self):
        return self.__icerdv


    

    def set_icercn(self, value):
        self.__icercn = value


    def set_icerfq(self, value):
        self.__icerfq = value


    def set_icermh(self, value):
        self.__icermh = value


    def set_icerxh(self, value):
        self.__icerxh = value


    def set_icerdv(self, value):
        self.__icerdv = value

class Icekel(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.icekcn = None
        self.icekfq = None
        self.icekmd = None
        self.icekxd = None
        

    def get_icekcn(self):
        return self.__icekcn


    def get_icekfq(self):
        return self.__icekfq


    def get_icekmd(self):
        return self.__icekmd


    def get_icekxd(self):
        return self.__icekxd


    

    def set_icekcn(self, value):
        self.__icekcn = value


    def set_icekfq(self, value):
        self.__icekfq = value


    def set_icekmd(self, value):
        self.__icekmd = value


    def set_icekxd(self, value):
        self.__icekxd = value

class Icedft(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.icedsp = None
        self.iceddr = None
        

    def get_icedsp(self):
        return self.__icedsp


    def get_iceddr(self):
        return self.__iceddr


    

    def set_icedsp(self, value):
        self.__icedsp = value


    def set_iceddr(self, value):
        self.__iceddr = value

class Icefra(IceFeature):
    
    def __init__(self):
        
        IceFeature.__init__(self)
        self.icefty = None
        self.iceloc = None
        self.ia_obn = None
        self.icesod = None
        self.icedvw = None
        self.ia_dmw = None
        self.ia_dxw = None
        

    def get_icefty(self):
        return self.__icefty


    def get_iceloc(self):
        return self.__iceloc


    def get_ia_obn(self):
        return self.__ia_obn


    def get_icesod(self):
        return self.__icesod


    def get_icedvw(self):
        return self.__icedvw


    def get_ia_dmw(self):
        return self.__ia_dmw


    def get_ia_dxw(self):
        return self.__ia_dxw


    

    def set_icefty(self, value):
        self.__icefty = value


    def set_iceloc(self, value):
        self.__iceloc = value


    def set_ia_obn(self, value):
        self.__ia_obn = value


    def set_icesod(self, value):
        self.__icesod = value


    def set_icedvw(self, value):
        self.__icedvw = value


    def set_ia_dmw(self, value):
        self.__ia_dmw = value


    def set_ia_dxw(self, value):
        self.__ia_dxw = value

class Icerft(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.icefcn = None
        

    def get_icefcn(self):
        return self.__icefcn


    

    def set_icefcn(self, value):
        self.__icefcn = value

class Jmdbrr(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        
class Stgmlt(IceFeature):
    
    
    def __init__(self):
        IceFeature.__init__(self)
        
        self.icemlt = None
        

    def get_icemlt(self):
        return self.__icemlt


    

    def set_icemlt(self, value):
        self.__icemlt = value

class Snwcvr(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.icescn = None
        self.icesct = None
        self.icedos = None
        
        
    def get_icescn(self):
        return self.__icescn


    def get_icesct(self):
        return self.__icesct


    def get_icedos(self):
        return self.__icedos


    

    def set_icescn(self, value):
        self.__icescn = value


    def set_icesct(self, value):
        self.__icesct = value


    def set_icedos(self, value):
        self.__icedos = value

class Strptc(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.icespc = None
        

    def get_icespc(self):
        return self.__icespc


    

    def set_icespc(self, value):
        self.__icespc = value

class I_Grhm(IceFeature):
    
    def __init__(self):
        IceFeature.__init__(self)
        self.ia_buh = None
        

    def get_ia_buh(self):
        return self.__ia_buh


    

    def set_ia_buh(self, value):
        self.__ia_buh = value


    
