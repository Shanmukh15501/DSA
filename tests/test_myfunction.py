import source.myfunction as myfunction
import pytest
import time 
import sys
import  unittest.mock   as mock
import source.shapes as shapes


def test_add():
    assert myfunction.add(5,4) == 9
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert myfunction.divide(1,0)

    
def test_divide():
    assert myfunction.divide(15,3) == 5
    
def test_add_strings():
    assert myfunction.add('15','3') == '153'


@pytest.mark.slow
def test_agent():
    time.sleep(1)
    assert True

@pytest.mark.slow
def test_tool():
    time.sleep(1)
    assert True

@pytest.mark.skip(reason="Works for linux only")
def test_pwd():
    assert True
    
@pytest.mark.skipif(sys.platform != "win32", reason="Does run on Windows")
def test_windows_only():
    assert True

@pytest.mark.xfail(reason="failed due to no response")
def test_zero_division():
    assert 4//0
    
@pytest.mark.lrf
@mock.patch("source.shapes.Circle.test_long_running")
def test_long_running(ans):
    ans.return_value =  100
    assert shapes.Circle(100).test_long_running() == 100
    
@pytest.mark.api   
@mock.patch("source.myfunction.requests.get")
def test_combined_api_calls(mock_get):
    def side_effect(url, *args, **kwargs):
        if "sqqqqqqqqqqqqq" in url:
            return mock.Mock(status_code=200, json=lambda: {"id": 1, "name": "Alice"})
        elif "sqqqqqqqqqqqqq" in url:
            return mock.Mock(status_code=200, json=lambda: {"id": 101, "item": "Book"})
    mock_get.side_effect = side_effect

    user = myfunction.fetch_user_data(1)
    order = myfunction.fetch_albums_data(1)

    assert user["name"] == "Alice"
    assert order["item"] == "Book"
    
@mock.patch("requests.get")
def test_user(mock_obj):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value =  {"id": 101, "item": "Book"}
    mock_obj.return_value = mock_response
    
    data = myfunction.fetch_user_data(1)
    
    assert data  ==  {"id": 101, "item": "Book"}
