import axios from 'axios';

export const HTTP = axios.create({
  baseURL: `localhost:5000`,
  headers: {
    crossorigin: true
  }
})