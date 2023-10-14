class ProjectsController < ApplicationController
  before_action :set_project, only: [:show, :update, :destroy]

  def index
    @projects = Project.all
    render json: @projects.serialized.as_json
  end

  def show
    render json: @project.serialized.as_json
  end

  def create
    @project = Project.new(project_params)
    if @project.save
      render json: @project.serialized.as_json, status: :created
    else
      render json: @project.errors, status: :unprocessable_entity
    end
  end

  def update
    if @project.update(project_params)
      render json: @project.serialized.as_json
    else
      render json: @project.errors, status: :unprocessable_entity
    end
  end

  def destroy
    @project.destroy
    head :no_content
  end

  private

  def set_project
    @project = Project.find(params[:id])
  end

  def project_params
    params.require(:project).permit(:title, :description, :content, :status)
  end
end
