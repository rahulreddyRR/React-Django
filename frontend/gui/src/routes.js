import React from 'react';
import {Route} from 'react-router-dom';
import ArticlesList from './containers/ArticleListview';
import ArticlesDetail from './containers/ArticleDetailView';

const BaseRouter =()=>(
    <div>
        <Route exact path='/' component={ArticlesList}/>
        <Route exact path='/:articleID' component={ArticlesDetail}/>
    </div>
);

export default BaseRouter