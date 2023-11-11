import React from 'react'
import ReactDOM from 'react-dom/client'

import { Layout } from './core/components/Layout.tsx'
import { Home } from './pages/home/Home.tsx'
import { Analysis } from './pages/analysis/Analysis.tsx'
import { MachineLearning } from './pages/machine-learning/MachineLearning.tsx'


ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Layout children={<Analysis></Analysis>}></Layout>
  </React.StrictMode>,
)
