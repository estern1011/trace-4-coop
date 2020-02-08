import About from './views/About'
import Home from './views/Home'
import Form from './views/Form'

const routes = [
  { path: "/", component: Home },
  { path: "/about", component: About },
  { path: "/submit", component: Form }
];

export default routes