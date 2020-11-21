SEARCH_RANDOM_ANIME_GENRE_QUERY = '''
query ($search: String, $page: Int, $amount: Int) {
  Page(page: $page, perPage: $amount) {
    pageInfo {
      total
      perPage
      currentPage
      lastPage
      hasNextPage
    }
    media(genre: $search, type: ANIME) {
      id
      idMal
      title {
        romaji
        english
        native
      }
      type
      format
      status
      description
      startDate {
        year
        month
        day
      }
      endDate {
        year
        month
        day
      }
      season
      seasonYear
      seasonInt
      episodes
      duration
      chapters
      volumes
      countryOfOrigin
      isLicensed
      source
      hashtag
      trailer {
        id
        site
        thumbnail
      }
      coverImage {
        extraLarge
        large
        medium
        color
      }
      bannerImage
      genres
      synonyms
      averageScore
      meanScore
      popularity
      isLocked
      trending
      favourites
      tags {
        id
        name
        description
        category
        rank
        isGeneralSpoiler
        isMediaSpoiler
        isAdult
      }
      relations {
        edges {
          id
          node {
            id
            siteUrl
            title {
              romaji
              english
              native
              userPreferred
            }
          }
        }
      }
      characters(sort:FAVOURITES_DESC) {
        edges {
          id
          node {
            id
            siteUrl
            name {
              first
              last
              full
              native
            }
          }
        }
      }
      staff(sort:FAVOURITES_DESC) {
        edges {
          id
          node {
            id
            siteUrl
            name {
              first
              last
              full
              native
            }
          }
        }
      }
      studios(isMain: true) {
        nodes {
        name	
        }
      }
      isAdult
      nextAiringEpisode {
        id
        airingAt
        timeUntilAiring
        episode
      }
      externalLinks {
        id
        url
        site
      }
      streamingEpisodes {
        title
        thumbnail
        url
        site
      }
      siteUrl
    }
  }
}
'''

SEARCH_RANDOM_ANIME_TAG_QUERY = '''
query ($search: String, $page: Int, $amount: Int) {
  Page(page: $page, perPage: $amount) {
    pageInfo {
      total
      perPage
      currentPage
      lastPage
      hasNextPage
    }
    media(tag: $search, type: ANIME) {
      id
      idMal
      title {
        romaji
        english
        native
      }
      type
      format
      status
      description
      startDate {
        year
        month
        day
      }
      endDate {
        year
        month
        day
      }
      season
      seasonYear
      seasonInt
      episodes
      duration
      chapters
      volumes
      countryOfOrigin
      isLicensed
      source
      hashtag
      trailer {
        id
        site
        thumbnail
      }
      coverImage {
        extraLarge
        large
        medium
        color
      }
      bannerImage
      genres
      synonyms
      averageScore
      meanScore
      popularity
      isLocked
      trending
      favourites
      tags {
        id
        name
        description
        category
        rank
        isGeneralSpoiler
        isMediaSpoiler
        isAdult
      }
      relations {
        edges {
          id
          node {
            id
            siteUrl
            title {
              romaji
              english
              native
              userPreferred
            }
          }
        }
      }
      characters(sort:FAVOURITES_DESC) {
        edges {
          id
          node {
            id
            siteUrl
            name {
              first
              last
              full
              native
            }
          }
        }
      }
      staff(sort:FAVOURITES_DESC) {
        edges {
          id
          node {
            id
            siteUrl
            name {
              first
              last
              full
              native
            }
          }
        }
      }
      studios(isMain: true) {
        nodes {
        name	
        }
      }
      isAdult
      nextAiringEpisode {
        id
        airingAt
        timeUntilAiring
        episode
      }
      externalLinks {
        id
        url
        site
      }
      streamingEpisodes {
        title
        thumbnail
        url
        site
      }
      siteUrl
    }
  }
}
'''

SEARCH_RANDOM_MANGA_GENRE_QUERY = '''
query ($search: String, $page: Int, $amount: Int) {
  Page(page: $page, perPage: $amount) {
    pageInfo {
      total
      perPage
      currentPage
      lastPage
      hasNextPage
    }
    media(genre: $search, type: MANGA) {
      id
      idMal
      title {
        romaji
        english
        native
      }
      type
      format
      status
      description
      startDate {
        year
        month
        day
      }
      endDate {
        year
        month
        day
      }
      season
      seasonYear
      seasonInt
      episodes
      duration
      chapters
      volumes
      countryOfOrigin
      isLicensed
      source
      hashtag
      trailer {
        id
        site
        thumbnail
      }
      coverImage {
        extraLarge
        large
        medium
        color
      }
      bannerImage
      genres
      synonyms
      averageScore
      meanScore
      popularity
      isLocked
      trending
      favourites
      tags {
        id
        name
        description
        category
        rank
        isGeneralSpoiler
        isMediaSpoiler
        isAdult
      }
      relations {
        edges {
          id
          node {
            id
            siteUrl
            title {
              romaji
              english
              native
              userPreferred
            }
          }
        }
      }
      characters(sort:FAVOURITES_DESC) {
        edges {
          id
          node {
            id
            siteUrl
            name {
              first
              last
              full
              native
            }
          }
        }
      }
      staff(sort:FAVOURITES_DESC) {
        edges {
          id
          node {
            id
            siteUrl
            name {
              first
              last
              full
              native
            }
          }
        }
      }
      studios(isMain: true) {
        nodes {
        name	
        }
      }
      isAdult
      nextAiringEpisode {
        id
        airingAt
        timeUntilAiring
        episode
      }
      externalLinks {
        id
        url
        site
      }
      streamingEpisodes {
        title
        thumbnail
        url
        site
      }
      siteUrl
    }
  }
}
'''

SEARCH_RANDOM_MANGA_TAG_QUERY = '''
query ($search: String, $page: Int, $amount: Int) {
  Page(page: $page, perPage: $amount) {
    pageInfo {
      total
      perPage
      currentPage
      lastPage
      hasNextPage
    }
    media(tag: $search, type: MANGA) {
      id
      idMal
      title {
        romaji
        english
        native
      }
      type
      format
      status
      description
      startDate {
        year
        month
        day
      }
      endDate {
        year
        month
        day
      }
      season
      seasonYear
      seasonInt
      episodes
      duration
      chapters
      volumes
      countryOfOrigin
      isLicensed
      source
      hashtag
      trailer {
        id
        site
        thumbnail
      }
      coverImage {
        extraLarge
        large
        medium
        color
      }
      bannerImage
      genres
      synonyms
      averageScore
      meanScore
      popularity
      isLocked
      trending
      favourites
      tags {
        id
        name
        description
        category
        rank
        isGeneralSpoiler
        isMediaSpoiler
        isAdult
      }
      relations {
        edges {
          id
          node {
            id
            siteUrl
            title {
              romaji
              english
              native
              userPreferred
            }
          }
        }
      }
      characters(sort:FAVOURITES_DESC) {
        edges {
          id
          node {
            id
            siteUrl
            name {
              first
              last
              full
              native
            }
          }
        }
      }
      staff(sort:FAVOURITES_DESC) {
        edges {
          id
          node {
            id
            siteUrl
            name {
              first
              last
              full
              native
            }
          }
        }
      }
      studios(isMain: true) {
        nodes {
        name	
        }
      }
      isAdult
      nextAiringEpisode {
        id
        airingAt
        timeUntilAiring
        episode
      }
      externalLinks {
        id
        url
        site
      }
      streamingEpisodes {
        title
        thumbnail
        url
        site
      }
      siteUrl
    }
  }
}
'''