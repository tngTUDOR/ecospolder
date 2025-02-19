from ..ecospold_base import *


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


class DatasetInformation(EcospoldBase):
    """DatasetInformation -- Contains the administrative information about the dataset at issue: type of dataset (unit process, elementary flow, impact category, multi-output process) timestamp, version and internalVersion number as well as language and localLanguage code.
    type -- Indicates the kind of data that is represented by this dataset.
    The code is: 0=System non-terminated. 1=Unit process. 2=System terminated. 3=Elementary flow. 4=Impact category.5=Multioutput process.
    'Unit process' contains the description of processes and their direct (in situ) elementary flows (emissions and resource consumption) and intermediate product flows (demand for energy carriers, waste treatment and transport services, working materials, etc.), so-called unit process raw data. Data that arrives at the ecoinvent database in the form of life cycle inventory results are nevertheless classified as unit process.
    'System non-terminated' is not used in the ecoinvent quality network.
    'System terminated' contains the cumulative elementary flows (i.e. the life cycle inventory result) of a unit process. This code is only used for datasets calculated within the ecoinvent database (LCI results).
    'Elementary flow' contains the definition of pollutants and of resources.
    'Impact category' contains the definition of the characterisation, damage or weighting factors of life cycle impact assessment methods.
    'Multioutput process' is a special kind of unit process, which delivers more than one product/service output.
    impactAssessmentResult -- Indicates whether or not (yes/no) the dataset contains the results of an impact assessment applied on unit processes (unit process raw data) or terminated systems (LCI results).
    timestamp -- Automatically generated date when dataset is created.
    version -- The ecoinvent version number is used as follows: with a major update (e.g. every second year) the version number is increased by one (1.00, 2.00, etc.). The digits after the decimal point (e.g., 1.01, 1.02, etc.) are used for minor updates (corrected errors) within the period of two major updates. The version number is placed manually.
    internalVersion -- The internalVersion number is used to discern different versions during the working period until the dataset is entered into the database). The internalVersion is generated automatically with each change made in the dataset or related file.
    energyValues -- Indicates the way energy values are used and applied in the dataset. The codes are: 0=Undefined. 1=Net values. 2=Gross values.
    This data field is by default set to 0 and not actively used in ecoinvent quality network.
    languageCode -- 2 letter ISO language codes are used. Default language is English. Lower case letters are used.
    localLanguageCode -- 2 letter ISO language codes are used. Default localLanguage is German. Lower case letters are used.

    """

    def __init__(
        self,
        type_=None,
        impactAssessmentResult=None,
        timestamp=None,
        version=None,
        internalVersion=None,
        energyValues=None,
        languageCode="en",
        localLanguageCode="de",
        gds_collector_=None,
        **kwargs_
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = ""
        self.type_ = _cast(int, type_)
        self.type__nsprefix_ = None
        self.impactAssessmentResult = _cast(bool, impactAssessmentResult)
        self.impactAssessmentResult_nsprefix_ = None
        if isinstance(timestamp, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
        else:
            initvalue_ = timestamp
        self.timestamp = initvalue_
        self.version = _cast(float, version)
        self.version_nsprefix_ = None
        self.internalVersion = _cast(float, internalVersion)
        self.internalVersion_nsprefix_ = None
        self.energyValues = _cast(int, energyValues)
        self.energyValues_nsprefix_ = None
        self.languageCode = _cast(None, languageCode)
        self.languageCode_nsprefix_ = None
        self.localLanguageCode = _cast(None, localLanguageCode)
        self.localLanguageCode_nsprefix_ = None

    def factory(*args_, **kwargs_):
        return DatasetInformation(*args_, **kwargs_)

    factory = staticmethod(factory)

    def validate_typeType(self, value):
        # Validate type typeType, a restriction on xsd:integer.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on typeType'
                    % {"value": value, "lineno": lineno}
                )
                result = False
            if value > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on typeType'
                    % {"value": value, "lineno": lineno}
                )
                result = False

    def validate_versionType(self, value):
        # Validate type versionType, a restriction on xsd:float.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (float)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if not self.gds_validate_simple_patterns(
                self.validate_versionType_patterns_, value
            ):
                self.gds_collector_.add_message(
                    'Value "%s" does not match xsd pattern restrictions: %s'
                    % (
                        encode_str_2_3(value),
                        self.validate_versionType_patterns_,
                    )
                )

    validate_versionType_patterns_ = [["^(\\d{1,2} ?\\.?\\d{0,2})$"]]

    def validate_internalVersionType(self, value):
        # Validate type internalVersionType, a restriction on xsd:float.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (float)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if not self.gds_validate_simple_patterns(
                self.validate_internalVersionType_patterns_, value
            ):
                self.gds_collector_.add_message(
                    'Value "%s" does not match xsd pattern restrictions: %s'
                    % (
                        encode_str_2_3(value),
                        self.validate_internalVersionType_patterns_,
                    )
                )

    validate_internalVersionType_patterns_ = [["^(\\d{1,2}\\.\\d{1,2})$"]]

    def validate_energyValuesType(self, value):
        # Validate type energyValuesType, a restriction on xsd:integer.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on energyValuesType'
                    % {"value": value, "lineno": lineno}
                )
                result = False
            if value > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on energyValuesType'
                    % {"value": value, "lineno": lineno}
                )
                result = False

    def validate_ISOLanguageCode(self, value):
        # Validate type ISOLanguageCode, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            value = value
            enumerations = [
                "ab",
                "aa",
                "af",
                "sq",
                "am",
                "ar",
                "hy",
                "as",
                "ay",
                "az",
                "ba",
                "eu",
                "bn",
                "dz",
                "bh",
                "bi",
                "br",
                "bg",
                "my",
                "be",
                "km",
                "ca",
                "zh",
                "co",
                "hr",
                "cs",
                "da",
                "nl",
                "en",
                "eo",
                "et",
                "fo",
                "fa",
                "fj",
                "fi",
                "fr",
                "fy",
                "gl",
                "ka",
                "de",
                "el",
                "kl",
                "gn",
                "gu",
                "ha",
                "iw",
                "he",
                "hi",
                "hu",
                "is",
                "in",
                "id",
                "ia",
                "ie",
                "iu",
                "ik",
                "ga",
                "it",
                "ja",
                "jw",
                "kn",
                "ks",
                "kk",
                "rw",
                "ky",
                "rn",
                "ko",
                "ku",
                "lo",
                "la",
                "lv",
                "ln",
                "lt",
                "mk",
                "mg",
                "ms",
                "ml",
                "mt",
                "gv",
                "mi",
                "mr",
                "mo",
                "mn",
                "na",
                "ne",
                "no",
                "oc",
                "or",
                "om",
                "ps",
                "pl",
                "pt",
                "pa",
                "qu",
                "rm",
                "ro",
                "ru",
                "sm",
                "sg",
                "sa",
                "gd",
                "sr",
                "sh",
                "st",
                "tn",
                "sn",
                "sd",
                "si",
                "ss",
                "sk",
                "sl",
                "so",
                "es",
                "su",
                "sw",
                "sv",
                "tl",
                "tg",
                "ta",
                "tt",
                "te",
                "th",
                "bo",
                "ti",
                "to",
                "ts",
                "tr",
                "tk",
                "tw",
                "ug",
                "uk",
                "ur",
                "uz",
                "vi",
                "vo",
                "cy",
                "wo",
                "xh",
                "ji",
                "yi",
                "yo",
                "zu",
            ]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ISOLanguageCode'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False
            if len(value) != 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd length restriction on ISOLanguageCode'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def _hasContent(self):
        if ():
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01"',
        name_="DatasetInformation",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("DatasetInformation")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "DatasetInformation":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="DatasetInformation",
        )
        if self._hasContent():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="DatasetInformation",
                pretty_print=pretty_print,
            )
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="DatasetInformation",
    ):
        if self.type_ is not None and "type_" not in already_processed:
            already_processed.add("type_")
            outfile.write(
                ' type="%s"' % self.gds_format_integer(self.type_, input_name="type")
            )
        if (
            self.impactAssessmentResult is not None
            and "impactAssessmentResult" not in already_processed
        ):
            already_processed.add("impactAssessmentResult")
            outfile.write(
                ' impactAssessmentResult="%s"'
                % self.gds_format_boolean(
                    self.impactAssessmentResult, input_name="impactAssessmentResult"
                )
            )
        if self.timestamp is not None and "timestamp" not in already_processed:
            already_processed.add("timestamp")
            outfile.write(
                ' timestamp="%s"'
                % self.gds_format_datetime(self.timestamp, input_name="timestamp")
            )
        if self.version is not None and "version" not in already_processed:
            already_processed.add("version")
            outfile.write(
                ' version="%s"'
                % self.gds_format_float(self.version, input_name="version")
            )
        if (
            self.internalVersion is not None
            and "internalVersion" not in already_processed
        ):
            already_processed.add("internalVersion")
            outfile.write(
                ' internalVersion="%s"'
                % self.gds_format_float(
                    self.internalVersion, input_name="internalVersion"
                )
            )
        if self.energyValues is not None and "energyValues" not in already_processed:
            already_processed.add("energyValues")
            outfile.write(
                ' energyValues="%s"'
                % self.gds_format_integer(self.energyValues, input_name="energyValues")
            )
        if self.languageCode != "en" and "languageCode" not in already_processed:
            already_processed.add("languageCode")
            outfile.write(
                " languageCode=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.languageCode), input_name="languageCode"
                        )
                    ),
                )
            )
        if (
            self.localLanguageCode != "de"
            and "localLanguageCode" not in already_processed
        ):
            already_processed.add("localLanguageCode")
            outfile.write(
                " localLanguageCode=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.localLanguageCode),
                            input_name="localLanguageCode",
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01"',
        name_="DatasetInformation",
        fromsubclass_=False,
        pretty_print=True,
    ):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("type", node)
        if value is not None and "type" not in already_processed:
            already_processed.add("type")
            self.type_ = self.gds_parse_integer(value, node, "type")
            self.validate_typeType(self.type_)  # validate type typeType
        value = find_attr_value_("impactAssessmentResult", node)
        if value is not None and "impactAssessmentResult" not in already_processed:
            already_processed.add("impactAssessmentResult")
            if value in ("true", "1"):
                self.impactAssessmentResult = True
            elif value in ("false", "0"):
                self.impactAssessmentResult = False
            else:
                raise_parse_error(node, "Bad boolean attribute")
        value = find_attr_value_("timestamp", node)
        if value is not None and "timestamp" not in already_processed:
            already_processed.add("timestamp")
            try:
                self.timestamp = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError("Bad date-time attribute (timestamp): %s" % exp)
        value = find_attr_value_("version", node)
        if value is not None and "version" not in already_processed:
            already_processed.add("version")
            value = self.gds_parse_float(value, node, "version")
            self.version = value
            self.validate_versionType(self.version)  # validate type versionType
        value = find_attr_value_("internalVersion", node)
        if value is not None and "internalVersion" not in already_processed:
            already_processed.add("internalVersion")
            value = self.gds_parse_float(value, node, "internalVersion")
            self.internalVersion = value
            self.validate_internalVersionType(
                self.internalVersion
            )  # validate type internalVersionType
        value = find_attr_value_("energyValues", node)
        if value is not None and "energyValues" not in already_processed:
            already_processed.add("energyValues")
            self.energyValues = self.gds_parse_integer(value, node, "energyValues")
            self.validate_energyValuesType(
                self.energyValues
            )  # validate type energyValuesType
        value = find_attr_value_("languageCode", node)
        if value is not None and "languageCode" not in already_processed:
            already_processed.add("languageCode")
            self.languageCode = value
            self.validate_ISOLanguageCode(
                self.languageCode
            )  # validate type ISOLanguageCode
        value = find_attr_value_("localLanguageCode", node)
        if value is not None and "localLanguageCode" not in already_processed:
            already_processed.add("localLanguageCode")
            self.localLanguageCode = value
            self.validate_ISOLanguageCode(
                self.localLanguageCode
            )  # validate type ISOLanguageCode

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        pass


# end class DatasetInformation
