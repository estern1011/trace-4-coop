import About from './views/About'
import Home from './views/Home'
import InterviewForm from './views/InterviewForm'
import CoopForm from './views/CoopForm'
import CompanyPage from './views/CompanyPage'
import Thanks from './views/Thanks'
import CompanyForm from './views/CompanyForm'
import PositionForm from './views/PositionForm'
import Position from './views/Position'

const routes = [
  { path: "/", component: Home },
  { path: "/about", component: About },
  { path: "/interview", component: InterviewForm },
  { path: "/coop", component: CoopForm },
  { path: "/companies/:company_name", name: 'companies', component: CompanyPage},
  { path: "/thanks", component: Thanks},
  { path: "/company", component: CompanyForm},
  { path: "/company/:company_name/add_position", name: 'positions', component: PositionForm},
  { path: "/companies/:company_name/:position_name/position", name: 'reviews', component: Position}
];

export default routes