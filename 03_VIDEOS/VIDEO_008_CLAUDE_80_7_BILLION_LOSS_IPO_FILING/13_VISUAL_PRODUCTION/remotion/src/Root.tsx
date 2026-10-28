import React from 'react';
import {Folder, Still} from 'remotion';
import {graphics} from './data';
import {GraphicFrame} from './GraphicFrame';

export const Root: React.FC=()=> <Folder name="VIDEO008-Graphics">{graphics.map(g=><Still key={g.scene} id={`VIDEO008-${g.scene}`} component={GraphicFrame} width={1920} height={1080} defaultProps={g}/>)}</Folder>;
