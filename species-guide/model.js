(function(root){
  'use strict';
  const normalize = value => String(value).toLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-z0-9]+/g,' ').trim();
  const synonyms = {tiny:'small',big:'large',huge:'large',magic:'magical',animal:'beasts',animals:'beasts',humanoid:'humanoids',goblinoid:'goblinoids'};
  function distance(a,b){let row=Array.from({length:b.length+1},(_,i)=>i);for(let i=1;i<=a.length;i++){let next=[i];for(let j=1;j<=b.length;j++)next[j]=Math.min(next[j-1]+1,row[j]+1,row[j-1]+(a[i-1]===b[j-1]?0:1));row=next;}return row[b.length];}
  function search(blocks,query){
    const q=normalize(query); if(!q)return blocks.slice();
    const terms=q.split(' ').map(t=>synonyms[t]||t);
    return blocks.map(block=>{const name=normalize(block.name);const text=normalize([block.name,...block.types,...block.size,block.commonality,...block.keywords,block.summary].join(' '));const literal=text.includes(q);const matched=terms.every(t=>text.includes(t));const typo=terms.length===1&&q.length>=4&&name.split(' ').some(t=>distance(t,q)<=1);return {block,score:name===q?100:literal?80:matched?60:typo?20:0};}).filter(x=>x.score).sort((a,b)=>b.score-a.score||a.block.name.localeCompare(b.block.name)).map(x=>x.block);
  }
  function browse(data,viewId,category,secondary){const view=data.views.find(v=>v.id===viewId)||data.views[0];return data.blocks.filter(b=>(view.id!=='type'||b.types.length>0)&&(!category||(Array.isArray(b[view.field])?b[view.field].includes(category):b[view.field]===category))&&(!secondary||(view.id==='type'?b.size.includes(secondary):b.types.includes(secondary))));}
  function readFilters(data,params){
    const values=(key,allowed,fallback=[])=>[...new Set((params.has(key)?params.getAll(key).flatMap(v=>v.split(',')):fallback).filter(v=>allowed.includes(v)))];
    const sizeView=params.get('view')==='size';
    return {type:values('type',data.views[0].options,[params.get(sizeView?'filter':'category')]),size:values('size',data.views[1].options,[params.get(sizeView?'category':'filter')]),common:values('common',data.commonality)};
  }
  function filterBlocks(blocks,selections){return blocks.filter(b=>(!selections.type.length||selections.type.some(v=>b.types.includes(v)))&&(!selections.size.length||selections.size.some(v=>b.size.includes(v)))&&(!selections.common.length||selections.common.includes(b.commonality)));}
  root.GuideModel={normalize,search,browse,readFilters,filterBlocks};
})(typeof window==='undefined'?globalThis:window);
