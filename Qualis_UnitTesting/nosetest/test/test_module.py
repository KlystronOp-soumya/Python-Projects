import re
import os
import sys

sys.path.append(os.getcwd())

from mytest import test_circle
import autopep8
from xml.etree import ElementTree
import pytest
import inspect


@pytest.fixture
def inspect_get_sourcecode(obj):
    source_without_comment = re.sub(r"\s*\#.*", " ", inspect.getsource(obj))
    if inspect.getdoc(obj):
        return inspect.cleandoc(source_without_comment).replace(inspect.getdoc(obj), "").replace('"""', "")
    return source_without_comment


@pytest.fixture
def get_xml_root_element(source):
    xml = ElementTree.parse(source)
    root = xml.getroot()
    return root


@pytest.mark.parametrize("obj, expected",
                         [(test_circle.TestingCircleCreation.test_creating_circle_with_numeric_radius,
                           [r"Circle\(2.5\)", r"((assert_equals|eq_)\(.+,\s*2.5\)|(assert_equals|eq_)\(2.5,\s*.+\))"]),
                          (test_circle.TestingCircleCreation.test_creating_circle_with_negative_radius,
                           [r"assert_raises\(ValueError", r"Circle\(-2.5\)",
                            r"((assert_equals|eq_)\(.+,\s*\"radius must be between 0 and 1000 inclusive\"\)|(assert_equals|eq_)\(\"radius must be between 0 and 1000 inclusive\",\s*.+\))"]),
                          (test_circle.TestingCircleCreation.test_creating_circle_with_greaterthan_radius,
                           [r"assert_raises\(ValueError", r"Circle\(1000.1\)",
                            r"((assert_equals|eq_)\(.+,\s*\"radius must be between 0 and 1000 inclusive\"\)|(assert_equals|eq_)\(\"radius must be between 0 and 1000 inclusive\",\s*.+\))"]),
                          (test_circle.TestingCircleCreation.test_creating_circle_with_nonnumeric_radius,
                           [r"assert_raises\(TypeError", r"Circle\(\"hello\"\)",
                            r"((assert_equals|eq_)\(.+,\s*\"radius must be a number\"\)|(assert_equals|eq_)\(\"radius must be a number\",\s*.+\))"]),
                          (test_circle.TestCircleArea.test_circlearea_with_random_numeric_radius,
                           [r"area()", r"Circle\(2.5\)",
                            r"((assert_equals|eq_)\(.+,\s*19.63\)|(assert_equals|eq_)\(19.63,\s*.+\))"]),
                          (test_circle.TestCircleArea.test_circlearea_with_min_radius,
                           [r"area()", r"Circle\(0[.0]*\)",
                            r"((assert_equals|eq_)\(.+,\s*0[.0]*\)|(assert_equals|eq_)\(0[.0]*,\s*.+\))"]),
                          (test_circle.TestCircleArea.test_circlearea_with_max_radius,
                           [r"area()", r"Circle\(1000[.0]*\)",
                            r"((assert_equals|eq_)\(.+,\s*3141592.65\)|(assert_equals|eq_)\(3141592.65,\s*.+\))"]),
                          (test_circle.TestCircleCircumference.test_circlecircum_with_random_numeric_radius,
                           [r"circumference()", r"Circle\(2.5\)",
                            r"((assert_equals|eq_)\(.+,\s*15.71\)|(assert_equals|eq_)\(15.71,\s*.+\))"]),
                          (test_circle.TestCircleCircumference.test_circlecircum_with_min_radius,
                           [r"circumference()", r"Circle\(0[.0]*\)",
                            r"((assert_equals|eq_)\(.+,\s*0[.0]*\)|(assert_equals|eq_)\(0[.0]*,\s*.+\))"]),
                          (test_circle.TestCircleCircumference.test_circlecircum_with_max_radius,
                           [r"circumference()", r"Circle\(1000[.0]*\)",
                            r"((assert_equals|eq_)\(.+,\s*6283.19\)|(assert_equals|eq_)\(6283.19,\s*.+\))"])],
                         ids=['test_tescases1', 'test_tescases2', 'test_tescases3', 'test_tescases4', 'test_tescases5',
                              'test_tescases6', 'test_tescases7', 'test_tescases8', 'test_tescases9', 'test_tescases10'])
def test_source_code(inspect_get_sourcecode, expected):
    code = autopep8.fix_code(inspect_get_sourcecode).replace("'", '"')
    for exp in expected:
        assert bool(re.search(exp, code))


@pytest.mark.parametrize("source, expected",
                         [("nosetests.xml", 10)], ids=['test_testcase_result'])
def test_nose_testcase_result(get_xml_root_element, expected):
    test_case_success = int(get_xml_root_element.attrib["tests"]) - int(get_xml_root_element.attrib["failures"]) - int(
        get_xml_root_element.attrib["errors"]) - int(get_xml_root_element.attrib["skip"])
    assert int(get_xml_root_element.attrib["tests"]) == expected and test_case_success == expected
