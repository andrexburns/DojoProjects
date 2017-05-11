require 'test_helper'

class UsersControllerTest < ActionController::TestCase
  test "should get dash" do
    get :dash
    assert_response :success
  end

end
