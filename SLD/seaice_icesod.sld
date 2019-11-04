<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd" xmlns:se="http://www.opengis.net/se">
  <NamedLayer>
    <se:Name>seaice</se:Name>
    <UserStyle>
      <se:Name>seaice</se:Name>
      <se:FeatureTypeStyle>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '99'</se:Description>
          <se:Title>Undetermined/Unknown</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>99</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PointSymbolizer>
            <se:Graphic>
              <se:Mark>
                <OnlineResource xlink:type="simple" xlink:href="ttf://Arial"/>
                <Format>ttf</Format>
                <se:MarkIndex>63</se:MarkIndex>
                <se:Fill>
                  <se:SvgParameter name="fill">#000000</se:SvgParameter>
                </se:Fill>
              </se:Mark>
              <se:Size>4.23333</se:Size>
            </se:Graphic>
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '98'</se:Description>
          <se:Title>Glacier Ice</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>98</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:GraphicFill>
                <se:Graphic>
                  <se:Mark>
                    <se:WellKnownName>equilateral_triangle</se:WellKnownName>
                    <se:Fill>
                      <se:SvgParameter name="fill">#ff0000</se:SvgParameter>
                    </se:Fill>
                    <se:Stroke>
                      <se:SvgParameter name="stroke">#ff0000</se:SvgParameter>
                    </se:Stroke>
                  </se:Mark>
                  <se:Size>3</se:Size>
                  <se:Displacement>
                    <se:DisplacementX>-3</se:DisplacementX>
                    <se:DisplacementY>3</se:DisplacementY>
                  </se:Displacement>
                </se:Graphic>
              </se:GraphicFill>
            </se:Fill>
            <VendorOption name="distance">15,15</VendorOption>
          </se:PolygonSymbolizer>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:GraphicFill>
                <se:Graphic>
                  <se:Mark>
                    <se:WellKnownName>equilateral_triangle</se:WellKnownName>
                    <se:Fill>
                      <se:SvgParameter name="fill">#ff0000</se:SvgParameter>
                    </se:Fill>
                    <se:Stroke>
                      <se:SvgParameter name="stroke">#ff0000</se:SvgParameter>
                    </se:Stroke>
                  </se:Mark>
                  <se:Size>3</se:Size>
                  <se:Displacement>
                    <se:DisplacementX>3</se:DisplacementX>
                    <se:DisplacementY>-3</se:DisplacementY>
                  </se:Displacement>
                </se:Graphic>
              </se:GraphicFill>
            </se:Fill>
            <VendorOption name="distance">15,15</VendorOption>
          </se:PolygonSymbolizer>
        </se:Rule>
<!-- JH: ICESOD=1, -->
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '1'</se:Description>
           <se:Title>ice free</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>1</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#96c8ff</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
<!-- JH: ICESOD=70, -->
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '70'</se:Description>
          <se:Title>Brash ice</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>70</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#96c8ff</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
<!-- JH: ICESOD=80, -->
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '80'</se:Description>
          <se:Title>No stage of development</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>80</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#96c8ff</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '81'</se:Description>
          <se:Title>New ice</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>81</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#f0d2fa</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '82'</se:Description>
          <se:Title>Nilas ice rind</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>82</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#ff64ff</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '83'</se:Description>
          <se:Title>Young Ice</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>83</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#aa28f0</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '84'</se:Description>
          <se:Title>Grey ice</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>84</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#873cd7</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '85'</se:Description>
          <se:Title>Grey-white ice</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>85</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#dc50eb</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '86'</se:Description>
          <se:Title>First year ice</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>86</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#ffff00</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '87'</se:Description>
          <se:Title>Thin first year ice</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>87</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#ffd200</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '88'</se:Description>
          <se:Title>Thin first year ice stage 1</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>88</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#d7fa82</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '89'</se:Description>
          <se:Title>Thin first year ice stage 2</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>89</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#affa00</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '91'</se:Description>
          <se:Title>Medium first year ice</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>91</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#00c814</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '93'</se:Description>
          <se:Title>Thick First Year Ice</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>93</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#007800</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '94'</se:Description>
          <se:Title>Residual ice</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>94</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#007800</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '95'</se:Description>
          <se:Title>Old ice</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>95</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#b46432</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '96'</se:Description>
          <se:Title>Second year ice</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>96</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#ff780a</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name></se:Name>
          <se:Description>icesod is '97'</se:Description>
          <se:Title>Multi-year ice</se:Title>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:Function name="regexp_match">
              <ogc:PropertyName>icesod</ogc:PropertyName>
              <ogc:Literal>97</ogc:Literal>
            </ogc:Function>
          </ogc:Filter>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:SvgParameter name="fill">#c80000</se:SvgParameter>
            </se:Fill>
          </se:PolygonSymbolizer>
        </se:Rule>
      </se:FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
