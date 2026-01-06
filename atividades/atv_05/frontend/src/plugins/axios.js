import axios from 'axios';

// Login e salva o token no localStorage
export async function login(username, password) {
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/token/', {
      username,
      password
    });

    var TOKEN = response.data.access;
    localStorage.setItem('TOKEN', TOKEN); // salva token
    return TOKEN;
  } catch (error) {
    console.log('Erro no login:', error.response?.data || error);
    throw error;
  }
}

// Função para verificar se está logado
export function verificarLogin() {
  const token = localStorage.getItem('TOKEN');
  return !!token; // retorna true se tiver token
}

// Buscar quartos usando token JWT
export async function quartos() {
  try {
    const response = await axios.get('http://127.0.0.1:8000/quarto/', {
    });

    return response.data;
  } catch (error) {
    console.log('Erro ao buscar quartos:', error.response?.data || error);
    return [];
  }
}
export async function addRoom(dados) {
  try {
    const response = await axios.post('http://127.0.0.1:8000/quarto/,',
      dados
    )
    return response.data
  } catch (error) {
    console.log("Não foi possível acessar a API de quartos");
    throw error;
  }
}

export async function addFuncionario(dados) {
  try {
    const response = await axios.post('http://127.0.0.1:8000/Funcionario/',
      dados
    )
    return response.data
  } catch (error) {
    alert("Não foi possível acessar a API de funcionários");
    throw error;
  }
}
