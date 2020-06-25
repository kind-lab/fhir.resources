#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2019-05-14.
#  2019, SMART Health IT.


import io
import json
import os
import unittest

from . import observation
from .fhirdate import FHIRDate


class ObservationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Observation", js["resourceType"])
        return observation.Observation(js)

    def testObservation1(self):
        inst = self.instantiate_from("obs-genetics-example3-mutationlist-4.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation1(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation1(inst2)

    def implObservation1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "49874-1")
        self.assertEqual(inst.code.coding[0].display, "ABCB4 gene mutation analysis")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].code.coding[0].code, "53037-8")
        self.assertEqual(
            inst.component[0].code.coding[0].display,
            "Genetic disease sequence variation interpretation",
        )
        self.assertEqual(inst.component[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(
            inst.component[0].valueCodeableConcept.coding[0].code, "LA6675-8"
        )
        self.assertEqual(
            inst.component[0].valueCodeableConcept.coding[0].display, "Benign"
        )
        self.assertEqual(
            inst.component[0].valueCodeableConcept.coding[0].system,
            "http://www.genenames.org",
        )
        self.assertEqual(
            inst.extension[0].url,
            "http://hl7.org/fhir/StructureDefinition/geneticsDNARegionName",
        )
        self.assertEqual(inst.extension[0].valueString, "intron 26")
        self.assertEqual(
            inst.extension[1].url,
            "http://hl7.org/fhir/StructureDefinition/geneticsVariationId",
        )
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].code, "31653")
        self.assertEqual(
            inst.extension[1].valueCodeableConcept.coding[0].display, "c.3487-16T>C"
        )
        self.assertEqual(
            inst.extension[1].valueCodeableConcept.coding[0].system,
            "http://www.ncbi.nlm.nih.gov/projects/SNP",
        )
        self.assertEqual(inst.id, "genetics-example3-mutationlist-4")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")

    def testObservation2(self):
        inst = self.instantiate_from("observation-example-f206-staphylococcus.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation2(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation2(inst2)

    def implObservation2(self, inst):
        self.assertEqual(inst.code.coding[0].code, "104177")
        self.assertEqual(inst.code.coding[0].display, "Blood culture")
        self.assertEqual(inst.code.coding[0].system, "http://acmelabs.org")
        self.assertEqual(inst.code.coding[1].code, "600-7")
        self.assertEqual(
            inst.code.coding[1].display, "Bacteria identified in Blood by Culture"
        )
        self.assertEqual(inst.code.coding[1].system, "http://loinc.org")
        self.assertEqual(inst.id, "f206")
        self.assertEqual(inst.interpretation.coding[0].code, "POS")
        self.assertEqual(
            inst.interpretation.coding[0].system, "http://hl7.org/fhir/v2/0078"
        )
        self.assertEqual(inst.issued.date, FHIRDate("2013-03-11T10:28:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-03-11T10:28:00+01:00")
        self.assertEqual(inst.method.coding[0].code, "104177005")
        self.assertEqual(
            inst.method.coding[0].display,
            "Blood culture for bacteria, including anaerobic screen",
        )
        self.assertEqual(inst.method.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueCodeableConcept.coding[0].code, "3092008")
        self.assertEqual(
            inst.valueCodeableConcept.coding[0].display, "Staphylococcus aureus"
        )
        self.assertEqual(
            inst.valueCodeableConcept.coding[0].system, "http://snomed.info/sct"
        )

    def testObservation3(self):
        inst = self.instantiate_from("observation-example-f202-temperature.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation3(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation3(inst2)

    def implObservation3(self, inst):
        self.assertEqual(inst.bodySite.coding[0].code, "74262004")
        self.assertEqual(inst.bodySite.coding[0].display, "Oral cavity")
        self.assertEqual(inst.bodySite.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.coding[0].code, "BT")
        self.assertEqual(inst.code.coding[0].display, "Body temperature")
        self.assertEqual(inst.code.coding[0].system, "http://acme.lab")
        self.assertEqual(inst.code.coding[1].code, "8310-5")
        self.assertEqual(inst.code.coding[1].display, "Body temperature")
        self.assertEqual(inst.code.coding[1].system, "http://loinc.org")
        self.assertEqual(inst.code.coding[2].code, "56342008")
        self.assertEqual(inst.code.coding[2].display, "Temperature taking")
        self.assertEqual(inst.code.coding[2].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Body temperature")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.interpretation.coding[0].code, "H")
        self.assertEqual(
            inst.interpretation.coding[0].system, "http://hl7.org/fhir/v2/0078"
        )
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-04T13:27:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-04T13:27:00+01:00")
        self.assertEqual(inst.method.coding[0].code, "89003005")
        self.assertEqual(inst.method.coding[0].display, "Oral temperature taking")
        self.assertEqual(inst.method.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.referenceRange[0].low.unit, "degrees C")
        self.assertEqual(inst.referenceRange[0].low.value, 37.5)
        self.assertEqual(inst.status, "entered-in-error")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "258710007")
        self.assertEqual(inst.valueQuantity.system, "http://snomed.info/sct")
        self.assertEqual(inst.valueQuantity.unit, "degrees C")
        self.assertEqual(inst.valueQuantity.value, 39)

    def testObservation4(self):
        inst = self.instantiate_from("observation-example-glasgow-qa.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation4(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation4(inst2)

    def implObservation4(self, inst):
        self.assertEqual(inst.code.coding[0].code, "9269-2")
        self.assertEqual(inst.code.coding[0].display, "Glasgow coma score total")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Glasgow Coma Scale , (GCS)")
        self.assertEqual(
            inst.effectiveDateTime.date, FHIRDate("2014-12-11T04:44:16Z").date
        )
        self.assertEqual(inst.effectiveDateTime.as_json(), "2014-12-11T04:44:16Z")
        self.assertEqual(inst.id, "gcs-qa")
        self.assertEqual(inst.referenceRange[0].high.code, "{score}")
        self.assertEqual(
            inst.referenceRange[0].high.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(inst.referenceRange[0].high.value, 8)
        self.assertEqual(inst.referenceRange[0].meaning.text, "Severe TBI")
        self.assertEqual(inst.referenceRange[1].high.code, "{score}")
        self.assertEqual(
            inst.referenceRange[1].high.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(inst.referenceRange[1].high.value, 12)
        self.assertEqual(inst.referenceRange[1].low.code, "{score}")
        self.assertEqual(inst.referenceRange[1].low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[1].low.value, 9)
        self.assertEqual(inst.referenceRange[1].meaning.text, "Moderate TBI")
        self.assertEqual(inst.referenceRange[2].low.code, "{score}")
        self.assertEqual(inst.referenceRange[2].low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[2].low.value, 13)
        self.assertEqual(inst.referenceRange[2].meaning.text, "Mild TBI")
        self.assertEqual(inst.related[0].type, "derived-from")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "{score}")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.value, 13)

    def testObservation5(self):
        inst = self.instantiate_from("obs-genetics-example3-mutationlist-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation5(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation5(inst2)

    def implObservation5(self, inst):
        self.assertEqual(inst.code.coding[0].code, "49874-1")
        self.assertEqual(inst.code.coding[0].display, "ABCB4 gene mutation analysis")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].code.coding[0].code, "53037-8")
        self.assertEqual(
            inst.component[0].code.coding[0].display,
            "Genetic disease sequence variation interpretation",
        )
        self.assertEqual(inst.component[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(
            inst.component[0].valueCodeableConcept.coding[0].code, "LA6682-4"
        )
        self.assertEqual(
            inst.component[0].valueCodeableConcept.coding[0].display,
            "Unknown significance",
        )
        self.assertEqual(
            inst.component[0].valueCodeableConcept.coding[0].system,
            "http://www.genenames.org",
        )
        self.assertEqual(
            inst.extension[0].url,
            "http://hl7.org/fhir/StructureDefinition/geneticsDNASequenceVariation",
        )
        self.assertEqual(inst.extension[0].valueString, "c.2708T>C")
        self.assertEqual(
            inst.extension[1].url,
            "http://hl7.org/fhir/StructureDefinition/geneticsDNARegionName",
        )
        self.assertEqual(inst.extension[1].valueString, "Exon 23")
        self.assertEqual(
            inst.extension[2].url,
            "http://hl7.org/fhir/StructureDefinition/geneticsAminoAcidChange",
        )
        self.assertEqual(inst.extension[2].valueString, "p.R969H")
        self.assertEqual(inst.id, "genetics-example3-mutationlist-1")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")

    def testObservation6(self):
        inst = self.instantiate_from("observation-example-bloodpressure.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation6(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation6(inst2)

    def implObservation6(self, inst):
        self.assertEqual(inst.bodySite.coding[0].code, "368209003")
        self.assertEqual(inst.bodySite.coding[0].display, "Right arm")
        self.assertEqual(inst.bodySite.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.coding[0].code, "55284-4")
        self.assertEqual(
            inst.code.coding[0].display, "Blood pressure systolic & diastolic"
        )
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].code.coding[0].code, "8480-6")
        self.assertEqual(
            inst.component[0].code.coding[0].display, "Systolic blood pressure"
        )
        self.assertEqual(inst.component[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].code.coding[1].code, "271649006")
        self.assertEqual(
            inst.component[0].code.coding[1].display, "Systolic blood pressure"
        )
        self.assertEqual(
            inst.component[0].code.coding[1].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.component[0].code.coding[2].code, "bp-s")
        self.assertEqual(
            inst.component[0].code.coding[2].display, "Systolic Blood pressure"
        )
        self.assertEqual(
            inst.component[0].code.coding[2].system,
            "http://acme.org/devices/clinical-codes",
        )
        self.assertEqual(inst.component[0].valueQuantity.unit, "mm[Hg]")
        self.assertEqual(inst.component[0].valueQuantity.value, 107)
        self.assertEqual(inst.component[1].code.coding[0].code, "8462-4")
        self.assertEqual(
            inst.component[1].code.coding[0].display, "Diastolic blood pressure"
        )
        self.assertEqual(inst.component[1].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[1].valueQuantity.unit, "mm[Hg]")
        self.assertEqual(inst.component[1].valueQuantity.value, 60)
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2012-09-17").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2012-09-17")
        self.assertEqual(inst.id, "blood-pressure")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(
            inst.identifier[0].value, "urn:uuid:187e0c12-8dd2-67e2-99b2-bf273c878281"
        )
        self.assertEqual(inst.interpretation.coding[0].code, "L")
        self.assertEqual(inst.interpretation.coding[0].display, "Below low normal")
        self.assertEqual(
            inst.interpretation.coding[0].system, "http://hl7.org/fhir/v2/0078"
        )
        self.assertEqual(inst.interpretation.text, "low")
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2014-01-30T22:35:23+11:00").date
        )
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2014-01-30T22:35:23+11:00")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")

    def testObservation7(self):
        inst = self.instantiate_from("obs-genetics-example3-mutationlist-3.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation7(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation7(inst2)

    def implObservation7(self, inst):
        self.assertEqual(inst.code.coding[0].code, "49874-1")
        self.assertEqual(inst.code.coding[0].display, "ABCB4 gene mutation analysis")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].code.coding[0].code, "53037-8")
        self.assertEqual(
            inst.component[0].code.coding[0].display,
            "Genetic disease sequence variation interpretation",
        )
        self.assertEqual(inst.component[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(
            inst.component[0].valueCodeableConcept.coding[0].code, "LA6675-8"
        )
        self.assertEqual(
            inst.component[0].valueCodeableConcept.coding[0].display, "Benign"
        )
        self.assertEqual(
            inst.component[0].valueCodeableConcept.coding[0].system,
            "http://www.genenames.org",
        )
        self.assertEqual(
            inst.extension[0].url,
            "http://hl7.org/fhir/StructureDefinition/geneticsDNARegionName",
        )
        self.assertEqual(inst.extension[0].valueString, "intron 16")
        self.assertEqual(
            inst.extension[1].url,
            "http://hl7.org/fhir/StructureDefinition/geneticsVariationId",
        )
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].code, "31668")
        self.assertEqual(
            inst.extension[1].valueCodeableConcept.coding[0].display, "c.2211+16C>T"
        )
        self.assertEqual(
            inst.extension[1].valueCodeableConcept.coding[0].system,
            "http://www.ncbi.nlm.nih.gov/projects/SNP",
        )
        self.assertEqual(inst.id, "genetics-example3-mutationlist-3")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")

    def testObservation8(self):
        inst = self.instantiate_from("observation-example-f005-hemoglobin.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation8(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation8(inst2)

    def implObservation8(self, inst):
        self.assertEqual(inst.code.coding[0].code, "718-7")
        self.assertEqual(
            inst.code.coding[0].display, "Hemoglobin [Mass/volume] in Blood"
        )
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(
            inst.effectivePeriod.end.date, FHIRDate("2013-04-05T10:30:10+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.end.as_json(), "2013-04-05T10:30:10+01:00"
        )
        self.assertEqual(
            inst.effectivePeriod.start.date, FHIRDate("2013-04-02T10:30:10+01:00").date
        )
        self.assertEqual(
            inst.effectivePeriod.start.as_json(), "2013-04-02T10:30:10+01:00"
        )
        self.assertEqual(inst.id, "f005")
        self.assertEqual(
            inst.identifier[0].system,
            "http://www.bmc.nl/zorgportal/identifiers/observations",
        )
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "6327")
        self.assertEqual(inst.interpretation.coding[0].code, "L")
        self.assertEqual(inst.interpretation.coding[0].display, "Below low normal")
        self.assertEqual(
            inst.interpretation.coding[0].system, "http://hl7.org/fhir/v2/0078"
        )
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-03T15:30:10+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-03T15:30:10+01:00")
        self.assertEqual(inst.referenceRange[0].high.code, "g/dL")
        self.assertEqual(
            inst.referenceRange[0].high.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(inst.referenceRange[0].high.unit, "g/dl")
        self.assertEqual(inst.referenceRange[0].high.value, 10)
        self.assertEqual(inst.referenceRange[0].low.code, "g/dL")
        self.assertEqual(inst.referenceRange[0].low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[0].low.unit, "g/dl")
        self.assertEqual(inst.referenceRange[0].low.value, 7.5)
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "g/dL")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.unit, "g/dl")
        self.assertEqual(inst.valueQuantity.value, 7.2)

    def testObservation9(self):
        inst = self.instantiate_from("observation-example-glasgow.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation9(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation9(inst2)

    def implObservation9(self, inst):
        self.assertEqual(inst.code.coding[0].code, "9269-2")
        self.assertEqual(inst.code.coding[0].display, "Glasgow coma score total")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Glasgow Coma Scale , (GCS)")
        self.assertEqual(inst.contained[0].id, "motor")
        self.assertEqual(inst.contained[1].id, "verbal")
        self.assertEqual(inst.contained[2].id, "eyes")
        self.assertEqual(
            inst.effectiveDateTime.date, FHIRDate("2014-12-11T04:44:16Z").date
        )
        self.assertEqual(inst.effectiveDateTime.as_json(), "2014-12-11T04:44:16Z")
        self.assertEqual(inst.id, "glasgow")
        self.assertEqual(inst.referenceRange[0].high.code, "{score}")
        self.assertEqual(
            inst.referenceRange[0].high.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(inst.referenceRange[0].high.value, 8)
        self.assertEqual(inst.referenceRange[0].meaning.text, "Severe TBI")
        self.assertEqual(inst.referenceRange[1].high.code, "{score}")
        self.assertEqual(
            inst.referenceRange[1].high.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(inst.referenceRange[1].high.value, 12)
        self.assertEqual(inst.referenceRange[1].low.code, "{score}")
        self.assertEqual(inst.referenceRange[1].low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[1].low.value, 9)
        self.assertEqual(inst.referenceRange[1].meaning.text, "Moderate TBI")
        self.assertEqual(inst.referenceRange[2].low.code, "{score}")
        self.assertEqual(inst.referenceRange[2].low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[2].low.value, 13)
        self.assertEqual(inst.referenceRange[2].meaning.text, "Mild TBI")
        self.assertEqual(inst.related[0].type, "derived-from")
        self.assertEqual(inst.related[1].type, "derived-from")
        self.assertEqual(inst.related[2].type, "derived-from")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "{score}")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.value, 13)

    def testObservation10(self):
        inst = self.instantiate_from("observation-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation10(inst)

        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation10(inst2)

    def implObservation10(self, inst):
        self.assertEqual(inst.category.coding[0].code, "vital-signs")
        self.assertEqual(inst.category.coding[0].display, "Vital Signs")
        self.assertEqual(
            inst.category.coding[0].system, "http://hl7.org/fhir/observation-category"
        )
        self.assertEqual(inst.code.coding[0].code, "3141-9")
        self.assertEqual(inst.code.coding[0].display, "Weight Measured")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.coding[1].code, "27113001")
        self.assertEqual(inst.code.coding[1].display, "Body weight")
        self.assertEqual(inst.code.coding[1].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.coding[2].code, "body-weight")
        self.assertEqual(inst.code.coding[2].display, "Body Weight")
        self.assertEqual(
            inst.code.coding[2].system, "http://acme.org/devices/clinical-codes"
        )
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "[lb_av]")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.unit, "lbs")
        self.assertEqual(inst.valueQuantity.value, 185)