import { api } from "./api"

export default {
    getProjects: async () => {
        try {
            const response = await api.get('projects');
            return response.data;
        } catch (error) {
            console.error('Erro ao obter projetos:', error);
            throw error;
        }
      },
      getProjectById: async (id) => {
        try {
          const response = await api.get(`projects/${id}`);
          return response.data;
        } catch (error) {
          console.error('Projeto não encontrado.', error);
          throw error;
        }
      }
}