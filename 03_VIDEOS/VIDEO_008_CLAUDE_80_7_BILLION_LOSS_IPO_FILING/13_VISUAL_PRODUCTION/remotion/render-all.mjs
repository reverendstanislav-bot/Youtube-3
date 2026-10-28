import {spawnSync} from 'node:child_process';
import {mkdirSync} from 'node:fs';
import {resolve} from 'node:path';

const scenes=['SC002','SC007','SC010','SC015','SC020','SC029','SC036','SC040','SC045','SC055','SC059','SC064','SC069','SC073','SC078','SC080','SC090','SC094','SC098','SC104','SC108'];
const out=process.env.VIDEO008_GRAPHICS_OUT || resolve('rendered');
mkdirSync(out,{recursive:true});
for(const scene of scenes){
  const args=[resolve('node_modules/@remotion/cli/remotion-cli.js'),'still','src/index.ts',`VIDEO008-${scene}`,resolve(out,`${scene}_EDITOR_GRAPHIC.png`),'--image-format=png','--overwrite','--browser-executable=C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'];
  const result=spawnSync(process.execPath,args,{stdio:'inherit',shell:false});
  if(result.error) throw result.error;
  if(result.status!==0) process.exit(result.status??1);
}
