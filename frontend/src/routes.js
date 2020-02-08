import About from './views/About'
import Home from './views/Home'
import CompanyPage from './views/CompanyPage'
import Position from './views/Position'


const routes = [
  { path: "/", component: Home },
  { path: "/about", component: About },
  { path: "/companies/:company_name", name: 'companies', component: CompanyPage},
];

export default routes