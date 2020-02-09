import About from './views/About'
import Home from './views/Home'
import InterviewForm from './views/InterviewForm'
import CoopForm from './views/CoopForm'
import CompanyPage from './views/CompanyPage'
import Thanks from './views/Thanks'
import CompanyForm from './views/CompanyForm'

const routes = [
  { path: "/", component: Home },
  { path: "/about", component: About },
  { path: "/interview", component: InterviewForm },
  { path: "/coop", component: CoopForm },
  { path: "/companies/:company_name", name: 'companies', component: CompanyPage},
  { path: "/thanks", component: Thanks},
  { path: "/company", component: CompanyForm}
];

export default routes