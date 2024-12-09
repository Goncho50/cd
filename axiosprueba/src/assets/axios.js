import axios from 'axios'


const axiosInstance = axios.create({

  baseURL: 'http://localhost:7050',

});


export default axiosInstance;