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
    if @project.destroy
      render json: @project.serialized.as_json, status: :no_content
    else
      render json: @project.errors, status: :unprocessable_entity
    end
  end

  private

  def set_project
    @project = Project.find(params[:id])
  end

  def project_params
    params.require(:project).permit(
      :title, :description, :content, :status, :name, :external_url,
      :short_description, :keywords, :start_at, :end_at, :phase
    )
  end
end
