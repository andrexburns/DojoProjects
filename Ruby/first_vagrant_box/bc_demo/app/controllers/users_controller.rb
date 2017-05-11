class UsersController < ApplicationController
  before_action :check_login
  
  def index
  end


  private


  def check_login
    if !session[:user_id]
      redirect_to '/'
    end
  end
end
