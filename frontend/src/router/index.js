import Vue from 'vue'
import Router from 'vue-router'

// Containers
const TheContainer = () => import('@/containers/TheContainer')

// Views
const shortURL = () => import('@/views/shortURL')

Vue.use(Router)

export default new Router({
  mode: 'hash', // https://router.vuejs.org/api/#mode
  linkActiveClass: 'active',
  scrollBehavior: () => ({ y: 0 }),
  routes: configRoutes()
})

function configRoutes () {
  return [
    {
      path: '/',
      redirect: '/shorturl',
      component: TheContainer,
      children: [
        {
          path: '/',
          redirect: 'shorturl',
          component: {
            render (c) { return c('router-view') }
          },
          children: [
            {
              path: 'shorturl',
              component: shortURL
            },
          ]
        },
      ]
    },
  ]
}

