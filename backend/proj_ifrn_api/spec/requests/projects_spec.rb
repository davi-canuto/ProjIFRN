require 'rails_helper'

RSpec.describe 'Projects', type: :request do
  describe 'GET /projects' do
    it 'returns a successful response' do
      get '/projects'
      expect(response).to have_http_status(200)
    end
  end

  describe 'POST /projects' do
    it 'creates a new project' do
      project_params = {
        project: {
          title: 'ProjIFRN', description: 'proj ifrn project', content: 'Content', status: 1
        }
      }

      post '/projects', params: project_params
      expect(response).to have_http_status(201)
    end
  end

  describe 'GET /projects/:id' do
    it 'returns a successful response' do
      project = Project.create(title: 'Test Project', description: 'Test Description', content: 'Test Content', status: 1)

      get "/projects/#{project.id}"
      expect(response).to have_http_status(200)
    end
  end

  describe 'PUT /projects/:id' do
    it 'updates a project' do
      project = Project.create(title: 'Test Project', description: 'Test Description', content: 'Test Content', status: 1)
      updated_params = { project: { title: 'Updated Project' } }

      put "/projects/#{project.id}", params: updated_params

      expect(response).to have_http_status(200)
      project.reload
      expect(project.title).to eq('Updated Project')
    end
  end

  describe 'DELETE /projects/:id' do
    it 'deletes a project' do
      project = Project.create(title: 'Test Project', description: 'Test Description', content: 'Test Content', status: 1)

      delete "/projects/#{project.id}"
      expect(response).to have_http_status(204)
    end
  end
end
