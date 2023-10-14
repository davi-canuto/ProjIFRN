require 'swagger_helper'

RSpec.describe 'projects', type: :request do
  path '/projects' do
    get('list projects') do
      response(200, 'successful') do
        let(:projects) { create_list(:project, 5) }

        after do |example|
          example.metadata[:response][:content] = {
            'application/json' => {
              example: JSON.parse(response.body, symbolize_names: true)
            }
          }
        end
        run_test!
      end
    end

    post('create project') do
      response(200, 'successful') do
        consumes 'application/json'
        parameter name: :project, in: :body, schema: {
          type: :object,
          properties: {
            name: { type: :string },
            description: { type: :string },
            content: { type: :string },
            status: { type: :integer }
          },
          required: %w[name description content status]
        }
        let(:project) { attributes_for(:project) }

        after do |example|
          example.metadata[:response][:content] = {
            'application/json' => {
              example: JSON.parse(response.body, symbolize_names: true)
            }
          }
        end
        run_test!
      end
    end
  end

  path '/projects/{id}' do
    parameter name: 'id', in: :path, type: :string, description: 'id'

    get('show project') do
      response(200, 'successful') do
        let(:project) { create(:project) }

        let(:id) { project.id }

        after do |example|
          example.metadata[:response][:content] = {
            'application/json' => {
              example: JSON.parse(response.body, symbolize_names: true)
            }
          }
        end
        run_test!
      end
    end

    put('update project') do
      response(200, 'successful') do
        consumes 'application/json'
        parameter name: :project, in: :body, schema: {
          type: :object,
          properties: {
            name: { type: :string },
            description: { type: :string },
            content: { type: :string },
            status: { type: :integer }
          },
          required: %w[name description content status]
        }
        let(:project) { create(:project) }

        let(:id) { project.id }

        after do |example|
          example.metadata[:response][:content] = {
            'application/json' => {
              example: JSON.parse(response.body, symbolize_names: true)
            }
          }
        end
        run_test!
      end
    end

    delete('delete project') do
      response(204, 'successful') do
        let(:project) { create(:project) }

        let(:id) { project.id }

        after do |example|
          example.metadata[:response][:content] = {
            'application/json' => {
              example: JSON.parse(response.body, symbolize_names: true)
            }
          }
        end
        run_test!
      end
    end
  end
end
