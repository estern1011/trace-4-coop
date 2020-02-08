import About from './views/About'
import Home from './views/Home'
import Form from './views/Form'
import CompanyPage from './views/CompanyPage'

const routes = [
  { path: "/", component: Home },
  { path: "/about", component: About },
  { path: "/submit", component: Form },
  { path: "/companies/:company_name", name: 'companies', component: CompanyPage}
];

export default routes