"""Test use of the meteogram module."""

from datetime import datetime
from numpy.testing import assert_almost_equal
from unittest import mock
import pytest
# from meteogram import meteogram
from meteogram import meteogram

# meteogram.

#
# Example starter test
#
def test_degF_to_degC_at_freezing():
    """
    Test if celsius conversion is correct at freezing.
    """
    # Setup
    freezing_degF = 32.0
    freezing_degC = 0.0

    # Exercise
    result = meteogram.degF_to_degC(freezing_degF)

    # Verify
    assert result == freezing_degC

    # Cleanup - none necessary

#
# Instructor led introductory examples
# string comparison basic test
#
def test_title_case():
    """
    Test string uppercasing function. Just a basic test example not related to library.
    """
    # setup
    input_str="this is test string"
    result_str="This Is Test String"
    # excersise
    actual = input_str.title()
    # verify
    assert actual == result_str
    # cleanup
    # none

#
# Instructor led examples of numerical comparison
#

#
# Exercise 1
#
def test_build_asos_request_url_single_digit_datetimes():
    """
    Test building URL with single digit month and day.
    """
    # setup, note -> if you change data value you need to adapt string
    start = datetime(2018,10,1,1)
    end = datetime(2018,11,1,1)
    station = "FSD"
    expected_url='https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?station%5B%5D=FSD&tz=UTC&year1=2018&month1=10&day1=01&hour1=01&minute1=00&year2=2018&month2=11&day2=01&hour2=01&minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes'
    # excersize
    url = meteogram.build_asos_request_url(station,start,end)
    # verify
    assert url == expected_url

def test_build_asos_request_url_double_digit_datetimes():
    """
    Test building URL with double digit month and day.
    """
    # setup, note -> if you change data value you need to adapt string
    start = datetime(2018,10,11,11)
    end = datetime(2018,10,16,11)
    station = "FSD"
    expected_url='https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?station%5B%5D=FSD&tz=UTC&year1=2018&month1=10&day1=11&hour1=11&minute1=00&year2=2018&month2=10&day2=16&hour2=11&minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes'
    # excersize
    url = meteogram.build_asos_request_url(station,start,end)
    # verify
    assert url == expected_url

#
# Exercise 2 - Add calculation tests here
#
def test_floating_substractions():
    # setup
    expected = 0.01
    # excersize
    calculated = 1 - 0.99
    # verify difference due to floating point numbers
    # assert abs(calculated - expected) < 0.0001
    # numpy has its own assertion suite for number
    assert_almost_equal(calculated,expected, decimal=3)

# def test_wind_components_north():
#     # setup
#     speed = 10
#     direction = 0 #deg
#     # exersize
#     u,v = meteogram.wind_components(speed, direction)
#     # assert
#     expect_u = 0
#     expect_v = 4
#     assert_almost_equal(u,except_u)
#     assert_almost_equal(v,except_v)

#
# Instructor led mock example
#
def mock_current_utc_time(y=2011,m=11,d=11,h=11):
    """
    Mock current utc time for testing with defaults
    """
    return datetime(y,m,d,h)
#
# Exercise 3 mock current date in the module
#
@mock.patch('meteogram.meteogram.current_utc_time',
    new=mock_current_utc_time)
def test_mock_current_utc_time():
    """
    Test if can know to use mock
    """

    result = meteogram.current_utc_time()

    expected = datetime(2011,11,11,11)

    assert result == expected

#
# Exercise 4 - compare images
# use remove_text to make it more robust because
# text might change due to lettertypes and other
# irrelevant changes
@pytest.mark.mpl_image_compare(remove_text=True)
def test_plotting_meteogram_defaults():
    # setup
    url = meteogram.build_asos_request_url('AMW',\
        start_date=datetime(2018,3,26),\
        end_date=datetime(2018,3,27))

    df = meteogram.download_asos_data(url)

    # print(df)
    if df.empty==False:
        # exersize
        fig,_,_,_ = meteogram.plot_meteogram(df)

        # verify - needs to return image to
        return fig
    else:
        Exception("No dataframe received from download_asos_data")

#
# Instructor led example of image testing
#

def load_example_asos():
    """
    Fixture to load sample data
    """

#
# Exercise 5
#

#
# Exercise 5 - Stop Here
#

#
# Exercise 6
#

#
# Exercise 6 - Stop Here
#

#
# Exercise 7
#

#
# Exercise 7 - Stop Here
#

# Demonstration of TDD here (time permitting)
