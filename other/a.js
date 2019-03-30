const octokit = new Octokit()
 
// Compare: https://developer.github.com/v3/repos/#list-organization-repositories
// const result = await octokit.git.listRefs({owner, repo, namespace, per_page, page})
// $("body").html(result)